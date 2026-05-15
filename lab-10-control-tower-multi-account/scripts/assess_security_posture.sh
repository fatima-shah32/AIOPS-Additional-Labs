#!/bin/bash

echo "========================================="
echo "Security Posture Assessment"
echo "========================================="

for account_dir in AWS_Accounts/*; do
  if [[ -d "$account_dir" ]]; then
    echo ""
    echo "Checking: $account_dir"

    if [[ -f "$account_dir/root_disabled" ]]; then
      echo "Root Account: COMPLIANT"
    else
      echo "Root Account: NON-COMPLIANT"
    fi

    if [[ -f "$account_dir/admin_mfa_enabled" ]]; then
      echo "MFA: COMPLIANT"
    else
      echo "MFA: NON-COMPLIANT"
    fi
  fi
done

echo ""
echo "Assessment Completed."
