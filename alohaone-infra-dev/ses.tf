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

# Apex TXT record. Holds multiple TXT strings at the zone apex — Route53
# treats these as a single TXT RRset with multiple values, so every new
# apex TXT has to be added to this one resource's `records` list rather
# than a new aws_route53_record (which would conflict on name+type).
#
# Current apex TXT strings:
#   1. SPF — unified sender policy that authorizes BOTH:
#        * Amazon SES (transactional mail from the Lambda — welcome,
#          billing, order confirmation, etc.)
#        * GoDaddy / M365 Exchange Online (user-sent mail from Outlook
#          when support@alohaone.ai is a real mailbox)
#      Using `~all` (soft-fail) during the transition period with two
#      independent senders. Tighten to `-all` once everything is settled.
#   2. MS= domain ownership verification for Microsoft 365 tenant.
resource "aws_route53_record" "ses_spf" {
  zone_id = local.zone_id
  name    = var.domain_name
  type    = "TXT"
  ttl     = 600
  records = [
    "v=spf1 include:amazonses.com include:secureserver.net ~all",
    "MS=ms44197346",
  ]
}

# ─────────────────────────────────────────────────────────────────────────────
# Microsoft 365 / GoDaddy Email records
# ─────────────────────────────────────────────────────────────────────────────
# These records complete the M365 mail setup for alohaone.ai so that
# support@alohaone.ai (and any future @alohaone.ai addresses) become real
# Exchange Online mailboxes — inbound mail lands in Outlook, replies work,
# calendar invites resolve, and Outlook clients auto-discover settings.
#
# NOTE: per GoDaddy/M365 guidance, any pre-existing MX records must be
# removed before email will start working. We had none.

resource "aws_route53_record" "m365_mx" {
  zone_id = local.zone_id
  name    = var.domain_name
  type    = "MX"
  ttl     = 600
  records = ["0 alohaone-ai.mail.protection.outlook.com"]
}

resource "aws_route53_record" "m365_autodiscover" {
  zone_id = local.zone_id
  name    = "autodiscover.${var.domain_name}"
  type    = "CNAME"
  ttl     = 600
  records = ["autodiscover.outlook.com"]
}

resource "aws_route53_record" "m365_email" {
  zone_id = local.zone_id
  name    = "email.${var.domain_name}"
  type    = "CNAME"
  ttl     = 600
  records = ["email.secureserver.net"]
}

# DMARC policy. Microsoft 365 (which hosts a lot of our target customers'
# inboxes) quarantines mail from new-domain senders that don't publish DMARC,
# so we need at least a permissive `p=none` record to avoid silently landing
# in junk. `rua` routes aggregate reports to an inbox we own so we can watch
# for auth failures during the first weeks of sending.
#
# Start with p=none (monitor mode) and tighten to p=quarantine or p=reject
# after we've verified every legitimate sending path is SPF/DKIM-aligned.
resource "aws_route53_record" "ses_dmarc" {
  zone_id = local.zone_id
  name    = "_dmarc.${var.domain_name}"
  type    = "TXT"
  ttl     = 600
  records = ["v=DMARC1; p=none; rua=mailto:support@alohaone.ai; fo=1"]
}

output "ses_domain_identity_arn" {
  description = "ARN of the SES domain identity for alohaone.ai. Referenced by downstream stacks that want to send email as support@alohaone.ai."
  value       = aws_ses_domain_identity.alohaone.arn
}
