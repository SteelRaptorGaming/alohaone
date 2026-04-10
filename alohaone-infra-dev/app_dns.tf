# ── ACM Certificate for app.alohaone.ai ──────────────────────────────────────
# DNS validated against the existing Route53 zone. Cert lives in us-east-1
# because CloudFront only accepts certs from us-east-1.

resource "aws_acm_certificate" "app" {
  domain_name       = "app.${var.domain_name}"
  validation_method = "DNS"
  tags              = merge(local.tags, { Name = "${local.name}-app-cert" })

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "app_cert_validation" {
  for_each = {
    for dvo in aws_acm_certificate.app.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  zone_id         = local.zone_id
  name            = each.value.name
  type            = each.value.type
  records         = [each.value.record]
  ttl             = 60
  allow_overwrite = true
}

resource "aws_acm_certificate_validation" "app" {
  certificate_arn         = aws_acm_certificate.app.arn
  validation_record_fqdns = [for r in aws_route53_record.app_cert_validation : r.fqdn]
}

# ── ALIAS records for app.alohaone.ai → CloudFront ───────────────────────────

resource "aws_route53_record" "app_a" {
  zone_id = local.zone_id
  name    = "app.${var.domain_name}"
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.app.domain_name
    zone_id                = aws_cloudfront_distribution.app.hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "app_aaaa" {
  zone_id = local.zone_id
  name    = "app.${var.domain_name}"
  type    = "AAAA"

  alias {
    name                   = aws_cloudfront_distribution.app.domain_name
    zone_id                = aws_cloudfront_distribution.app.hosted_zone_id
    evaluate_target_health = false
  }
}
