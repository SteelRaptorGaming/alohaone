# ── Origin Access Control for the app bucket ────────────────────────────────

resource "aws_cloudfront_origin_access_control" "app" {
  name                              = "${local.name}-app-oac"
  description                       = "OAC for ${local.name} app bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# ── CloudFront Distribution for app.alohaone.ai ──────────────────────────────

resource "aws_cloudfront_distribution" "app" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "${local.name} app shell (app.alohaone.ai)"
  default_root_object = "index.html"
  price_class         = "PriceClass_100"
  aliases             = ["app.${var.domain_name}"]
  tags                = merge(local.tags, { Name = "${local.name}-app-cdn" })

  origin {
    origin_id                = "s3-${aws_s3_bucket.app.id}"
    domain_name              = aws_s3_bucket.app.bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.app.id
  }

  default_cache_behavior {
    target_origin_id       = "s3-${aws_s3_bucket.app.id}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    # AWS-managed CachingOptimized policy
    cache_policy_id = "658327ea-f89d-4fab-a63d-7e88639e58f6"
  }

  # SPA routing fallback: 403/404 from S3 → /index.html so the shell handles
  # client-side routing for any path. Works because the shell is a single-page
  # app and unknown paths should fall through to the shell rather than 404.
  custom_error_response {
    error_code            = 403
    response_code         = 200
    response_page_path    = "/index.html"
    error_caching_min_ttl = 60
  }

  custom_error_response {
    error_code            = 404
    response_code         = 200
    response_page_path    = "/index.html"
    error_caching_min_ttl = 60
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate_validation.app.certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }
}
