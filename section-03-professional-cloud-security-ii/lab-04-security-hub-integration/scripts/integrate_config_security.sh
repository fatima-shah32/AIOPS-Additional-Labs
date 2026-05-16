#!/bin/bash
# Simulate AWS Config → Security Hub integration

CONFIG_FILE="mock_ec2_instance.json"
SECURITY_HUB_FILE="mock_security_finding.json"

if [ -f "$CONFIG_FILE" ]; then
  echo "Resource configuration tracked: $CONFIG_FILE"

  COMPLIANCE_STATUS="NON_COMPLIANT"
  echo "Sending finding to Security Hub: $COMPLIANCE_STATUS"

  cat "$SECURITY_HUB_FILE"
else
  echo "Resource configuration file not found."
fi
