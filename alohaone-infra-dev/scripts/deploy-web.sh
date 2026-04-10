#!/usr/bin/env bash
# Sync the AlohaOne marketing site (../../) to its S3 bucket and invalidate CloudFront.
# Reads bucket + distribution from `terraform output`.

set -euo pipefail

cd "$(dirname "$0")/.."

BUCKET="$(terraform output -raw site_bucket)"
DIST_ID="$(terraform output -raw cloudfront_distribution_id)"
SITE_DIR="$(cd .. && pwd)"

echo "Bucket:        $BUCKET"
echo "Distribution:  $DIST_ID"
echo "Source:        $SITE_DIR"
echo

# Sync everything except the infra dir, generator, git noise, and editor files.
# Long cache for hashed/static assets, short cache for HTML so updates show up fast.

aws s3 sync "$SITE_DIR" "s3://$BUCKET" \
  --delete \
  --exclude "alohaone-infra-dev/*" \
  --exclude ".git/*" \
  --exclude ".github/*" \
  --exclude ".vscode/*" \
  --exclude "*.py" \
  --exclude "*.md" \
  --exclude ".gitignore" \
  --exclude "*.html" \
  --cache-control "public,max-age=31536000,immutable"

aws s3 sync "$SITE_DIR" "s3://$BUCKET" \
  --exclude "*" \
  --include "*.html" \
  --content-type "text/html; charset=utf-8" \
  --cache-control "public,max-age=300,must-revalidate"

echo
echo "Invalidating CloudFront..."
aws cloudfront create-invalidation \
  --distribution-id "$DIST_ID" \
  --paths "/*" \
  --query 'Invalidation.Id' \
  --output text

echo
echo "Done. Site: $(terraform output -raw site_url)"
