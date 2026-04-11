# ─────────────────────────────────────────────────────────────────────────────
# SES domain identity for alohaone.ai
# ─────────────────────────────────────────────────────────────────────────────
# Every platform in the AlohaOne ecosystem sends transactional email via SES
# from some address at alohaone.ai (welcome email, password reset, billing
# receipts, etc.). Verifying the apex domain once here means any subaddress
# like `support@alohaone.ai` is immediately sendable — no per-address setup.
#
# Flow:
#   1. aws_ses_domain_identity registers alohaone.ai with SES
#   2. aws_ses_domain_dkim generates 3 DKIM selector tokens
#   3. aws_route53_record.ses_dkim publishes the 3 CNAMEs in the existing zone
#   4. aws_ses_domain_identity_verification blocks until SES sees the records
#      and marks the domain as verified
#   5. aws_route53_record.ses_spf publishes a TXT SPF record authorizing SES
#      to send on behalf of alohaone.ai
#
# The domain is shared between AlohaCommerce, AlohaBackup, AlohaOneApp, and
# future platforms — all of which send via the same SES API credentials from
# the same Lambda execution roles. No per-platform SES identity needed.

resource "aws_ses_domain_identity" "alohaone" {
  domain = var.domain_name  # "alohaone.ai"
}

resource "aws_ses_domain_dkim" "alohaone" {
  domain = aws_ses_domain_identity.alohaone.domain
}

resource "aws_route53_record" "ses_dkim" {
  count   = 3
  zone_id = local.zone_id
  name    = "${aws_ses_domain_dkim.alohaone.dkim_tokens[count.index]}._domainkey.${var.domain_name}"
  type    = "CNAME"
  ttl     = 600
  records = ["${aws_ses_domain_dkim.alohaone.dkim_tokens[count.index]}.dkim.amazonses.com"]
}

resource "aws_ses_domain_identity_verification" "alohaone" {
  domain     = aws_ses_domain_identity.alohaone.id
  depends_on = [aws_route53_record.ses_dkim]
}

# SPF record. Authorizes Amazon SES to send mail on behalf of alohaone.ai.
# The `~all` policy is soft-fail — recipient servers will accept but mark
# unauthorized senders as suspicious. Tighten to `-all` once we're confident
# no other senders need to act as alohaone.ai.
resource "aws_route53_record" "ses_spf" {
  zone_id = local.zone_id
  name    = var.domain_name
  type    = "TXT"
  ttl     = 600
  records = ["v=spf1 include:amazonses.com ~all"]
}

output "ses_domain_identity_arn" {
  description = "ARN of the SES domain identity for alohaone.ai. Referenced by downstream stacks that want to send email as support@alohaone.ai."
  value       = aws_ses_domain_identity.alohaone.arn
}
