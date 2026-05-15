#!/bin/bash

echo "Enforcing guardrails across all accounts..."

for account_dir in AWS_Accounts/*; do
  if [[ -d "$account_dir" ]]; then
    echo "Processing: $account_dir"
    ./lab-10-control-tower-multi-account/scripts/preventive_guardrails.sh
  fi
done

echo "All guardrails enforced."
