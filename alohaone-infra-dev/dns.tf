# ── Route53 Hosted Zone ──────────────────────────────────────────────────────
# Toggle off via create_route53_zone if a zone already exists for domain_name.

resource "aws_route53_zone" "site" {
  count = var.create_route53_zone ? 1 : 0
  name  = var.domain_name
  tags  = merge(local.tags, { Name = "${local.name}-zone" })
}

data "aws_route53_zone" "site" {
  count        = var.create_route53_zone ? 0 : 1
  name         = var.domain_name
  private_zone = false
}

locals {
  zone_id = var.create_route53_zone ? aws_route53_zone.site[0].zone_id : data.aws_route53_zone.site[0].zone_id
}

# ── ACM Certificate (must be us-east-1 for CloudFront) ──────────────────────
# All HTTPS-related resources are gated on enable_https. On a fresh deploy,
# set enable_https=false until the registrar is pointed at this zone, then
# re-apply with enable_https=true. See variables.tf for the bootstrap order.

resource "aws_acm_certificate" "site" {
  count                     = var.enable_https ? 1 : 0
  domain_name               = var.domain_name
  subject_alternative_names = var.include_www ? ["www.${var.domain_name}"] : []
  validation_method         = "DNS"
  tags                      = merge(local.tags, { Name = "${local.name}-cert" })

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "cert_validation" {
  for_each = var.enable_https ? {
    for dvo in aws_acm_certificate.site[0].domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  } : {}

  zone_id         = local.zone_id
  name            = each.value.name
  type            = each.value.type
  records         = [each.value.record]
  ttl             = 60
  allow_overwrite = true
}

resource "aws_acm_certificate_validation" "site" {
  count                   = var.enable_https ? 1 : 0
  certificate_arn         = aws_acm_certificate.site[0].arn
  validation_record_fqdns = [for r in aws_route53_record.cert_validation : r.fqdn]
}

# ── Apex + www ALIAS records → CloudFront ────────────────────────────────────
# Also gated on enable_https — without the cert covering these names, CloudFront
# would reject HTTPS requests for them anyway, and bare HTTP would 4xx because
# the distribution has no matching alias. While bootstrapping, the CloudFront
# default *.cloudfront.net domain is the only working URL.

resource "aws_route53_record" "apex_a" {
  count   = var.enable_https ? 1 : 0
  zone_id = local.zone_id
  name    = var.domain_name
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.site.domain_name
    zone_id                = aws_cloudfront_distribution.site.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "apex_aaaa" {
  count   = var.enable_https ? 1 : 0
  zone_id = local.zone_id
  name    = var.domain_name
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.site.domain_name
    zone_id                = aws_cloudfront_distribution.site.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "www_a" {
  count   = var.enable_https && var.include_www ? 1 : 0
  zone_id = local.zone_id
  name    = "www.${var.domain_name}"
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.site.domain_name
    zone_id                = aws_cloudfront_distribution.site.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "www_aaaa" {
  count   = var.enable_https && var.include_www ? 1 : 0
  zone_id = local.zone_id
  name    = "www.${var.domain_name}"
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.site.domain_name
    zone_id                = aws_cloudfront_distribution.site.hosted_zone_id
    evaluate_target_health = false
  }
}
