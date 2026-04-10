# alohaone-infra-dev

Terraform for the AlohaOne marketing site (alohaone.ai). Static S3 + CloudFront + ACM + Route53, deployed into the same AWS account and region (`us-east-1`) as AlohaCommerce.

A static site does not live inside a VPC — CloudFront is global and S3 is regional, so there is no VPC attachment to share with Commerce. Future server-side pieces would be added separately.

## Files

| File             | Purpose                                                  |
|------------------|----------------------------------------------------------|
| `providers.tf`   | AWS provider, random suffix                              |
| `variables.tf`   | Region, project, env, domain, www toggle, zone toggle    |
| `storage.tf`     | Private S3 bucket for site files (CloudFront origin)     |
| `cloudfront.tf`  | CloudFront distribution with OAC                         |
| `dns.tf`         | Route53 zone, ACM cert, validation, apex + www aliases   |
| `outputs.tf`     | Bucket, distribution id, CloudFront domain, nameservers  |
| `scripts/deploy-web.sh` | Sync site files from `..` and invalidate cache    |

## First-time deploy (two-stage)

ACM DNS validation requires the new Route53 zone to be reachable from the public internet, which means the registrar must already point at the four AWS nameservers before the cert is requested. On a brand-new domain that's never been delegated, you have to bootstrap in two `apply` calls:

```bash
cd alohaone-infra-dev
terraform init

# Stage 1: zone + bucket + CloudFront on the default cloudfront.net cert.
# No ACM cert, no custom-domain aliases. Apply takes ~3 minutes.
terraform apply -var enable_https=false

# Read the four AWS nameservers and set them at your registrar.
terraform output route53_nameservers
# ... update nameservers at registrar, wait for propagation ...

# Verify delegation has reached the .ai TLD before stage 2:
nslookup -type=NS alohaone.ai v0n0.nic.ai   # must show awsdns-* nameservers

# Stage 2: ACM cert + validation + custom-domain aliases. Cert validates in
# under a minute, then CloudFront updates in-place.
terraform apply

# Push the static site
./scripts/deploy-web.sh
```

If the domain is **already** delegated to a Route53 zone before you run Terraform (e.g., you imported an existing zone with `create_route53_zone=false`), you can skip stage 1 and run a single `terraform apply` with the default `enable_https=true`.

## Why no IP address

CloudFront does not expose a fixed IP. Route53 ALIAS records resolve `alohaone.ai` to the current set of CloudFront edge IPs at query time. The only thing you point at the registrar is the four NS records output by `terraform apply`.

## Updating the site

```bash
./scripts/deploy-web.sh
```

This re-syncs `../` to the bucket (excluding infra files, scripts, and markdown), sets long cache headers on assets and a short cache header on HTML, and creates a `/*` CloudFront invalidation.

## Disabling the Route53 zone (if one already exists)

Set `create_route53_zone = false` in `terraform.tfvars` and the existing zone will be looked up by name instead of created.
