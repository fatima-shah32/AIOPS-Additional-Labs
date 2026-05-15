#!/bin/bash
# Simulate Security Hub alert trigger

FINDING_FILE="mock_security_finding.json"

if [ -f "$FINDING_FILE" ]; then
  FINDING_STATUS=$(jq -r '.ComplianceStatus' "$FINDING_FILE")

  if [ "$FINDING_STATUS" == "NON_COMPLIANT" ]; then
    echo "🚨 ALERT: Security Hub detected a compliance violation!"
  else
    echo "No compliance violations detected."
  fi
else
  echo "Security finding file not found."
fi
