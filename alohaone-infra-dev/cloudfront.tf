# ── Origin Access Control ────────────────────────────────────────────────────

resource "aws_cloudfront_origin_access_control" "site" {
  name                              = "${local.name}-oac"
  description                       = "OAC for ${local.name} site bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# ── Distribution ─────────────────────────────────────────────────────────────

resource "aws_cloudfront_distribution" "site" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "${local.name} marketing site"
  default_root_object = "index.html"
  price_class         = "PriceClass_100"
  aliases             = var.enable_https ? local.site_aliases : []
  tags                = merge(local.tags, { Name = "${local.name}-cdn" })

  origin {
    origin_id                = "s3-${aws_s3_bucket.site.id}"
    domain_name              = aws_s3_bucket.site.bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.site.id
  }

  default_cache_behavior {
    target_origin_id       = "s3-${aws_s3_bucket.site.id}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    # AWS-managed CachingOptimized policy
    cache_policy_id = "658327ea-f89d-4fab-a63d-7e88639e58f6"
  }

  # Pretty-URL fallback: /platforms/commerce → /platforms/commerce.html
  # Static site has no SPA router, so map 403/404 from S3 to a friendly 404 page
  # served from the bucket. (S3 returns 403 for missing keys when listing is denied.)
  custom_error_response {
    error_code            = 403
    response_code         = 404
    response_page_path    = "/404.html"
    error_caching_min_ttl = 60
  }

  custom_error_response {
    error_code            = 404
    response_code         = 404
    response_page_path    = "/404.html"
    error_caching_min_ttl = 60
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = var.enable_https ? null : true
    acm_certificate_arn            = var.enable_https ? aws_acm_certificate_validation.site[0].certificate_arn : null
    ssl_support_method             = var.enable_https ? "sni-only" : null
    minimum_protocol_version       = var.enable_https ? "TLSv1.2_2021" : null
  }
}
