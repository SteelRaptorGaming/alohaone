#!/usr/bin/env bash
# Sync the AlohaOneApp shell (../../../AlohaOneApp/) to its S3 bucket and
# invalidate the app.alohaone.ai CloudFront distribution.
# Reads bucket + distribution from `terraform output`.

set -euo pipefail

cd "$(dirname "$0")/.."

BUCKET="$(terraform output -raw app_bucket)"
DIST_ID="$(terraform output -raw app_cloudfront_distribution_id)"
APP_DIR="$(cd ../../AlohaOneApp && pwd)"

echo "Bucket:        $BUCKET"
echo "Distribution:  $DIST_ID"
echo "Source:        $APP_DIR"
echo

# First sync: assets (CSS, JS, partials) with long cache.
# Second sync: HTML with short cache so changes show up fast.

aws s3 sync "$APP_DIR" "s3://$BUCKET" \
  --delete \
  --exclude "alohaoneapp-ui-tests/*" \
  --exclude "test-results/*" \
  --exclude "node_modules/*" \
  --exclude ".git/*" \
  --exclude ".github/*" \
  --exclude ".vscode/*" \
  --exclude "*.md" \
  --exclude ".gitignore" \
  --exclude "*.html" \
  --cache-control "public,max-age=31536000,immutable"

aws s3 sync "$APP_DIR" "s3://$BUCKET" \
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
echo "Done. App: $(terraform output -raw app_url)"
