output "site_bucket" {
  value       = aws_s3_bucket.site.bucket
  description = "S3 bucket holding the static site files. Sync your site here."
}

output "cloudfront_distribution_id" {
  value       = aws_cloudfront_distribution.site.id
  description = "CloudFront distribution ID (use for cache invalidations after a deploy)."
}

output "cloudfront_domain_name" {
  value       = aws_cloudfront_distribution.site.domain_name
  description = "CloudFront-assigned domain (dxxxx.cloudfront.net). Useful for direct testing before DNS propagates."
}

output "site_url" {
  value       = "https://${var.domain_name}"
  description = "Public URL once DNS resolves."
}

output "route53_nameservers" {
  value       = var.create_route53_zone ? aws_route53_zone.site[0].name_servers : null
  description = "Set these as the nameservers at your domain registrar for the configured domain_name."
}
