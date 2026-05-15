#!/bin/bash

echo "Applying Preventive Guardrails..."

# Root account lock simulation
touch AWS_Accounts/Root_Account/root_disabled

# MFA enforcement simulation
for dir in AWS_Accounts/*; do
  if [[ -d "$dir" ]]; then
    touch "$dir/admin_mfa_enabled"
  fi
done

echo "Preventive guardrails applied successfully."
