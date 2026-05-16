#!/bin/bash

RESULT=$(./check_instance_type.sh)

if [[ "$RESULT" == *"Non-Compliant"* ]]; then
  echo "ALERT: Compliance violation detected!"
else
  echo "No violations detected."
fi
