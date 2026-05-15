#!/bin/bash

POLICY="../policies/s3-access-policy.json"

echo "Simulating IAM integration with S3..."

if [ -f "$POLICY" ]; then
  echo "Permission GRANTED: S3 bucket access allowed (mybucket)"
else
  echo "Permission DENIED"
fi
