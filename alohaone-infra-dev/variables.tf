variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project" {
  type    = string
  default = "alohaone"
}

variable "env" {
  type    = string
  default = "dev"
}

# ── Site / DNS ───────────────────────────────────────────────────────────────

variable "domain_name" {
  type        = string
  description = "Apex domain for the marketing site (e.g. alohaone.ai)"
  default     = "alohaone.ai"
}

variable "include_www" {
  type        = bool
  description = "Also serve www.<domain_name> from the same distribution"
  default     = true
}

variable "create_route53_zone" {
  type        = bool
  description = "Create the Route53 hosted zone for domain_name. Set false if a zone already exists."
  default     = true
}

variable "enable_https" {
  type        = bool
  description = <<-EOT
    Provision the ACM cert and attach the custom-domain aliases (apex + www) to CloudFront.

    On a fresh deploy where the domain isn't yet delegated to the new Route53 zone,
    set this to false on the first apply, update the registrar nameservers from the
    route53_nameservers output, then re-apply with this set to true. This avoids the
    hour-long ACM validation hang that happens when Terraform tries to validate a cert
    against DNS records the public internet cannot yet see.
  EOT
  default     = true
}
