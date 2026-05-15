#!/bin/bash

POLICY="../policies/lambda-access-policy.json"

echo "Simulating IAM integration with Lambda..."

if [ -f "$POLICY" ]; then
  echo "Permission GRANTED: Lambda function can be invoked"
else
  echo "Permission DENIED"
fi
