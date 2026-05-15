#!/bin/bash

RESOURCE_FILE="../configs/mock_ec2_instance.json"
EXPECTED_INSTANCE_TYPE="t2.micro"

if [ -f "$RESOURCE_FILE" ]; then

  INSTANCE_TYPE=$(jq -r '.resourceConfiguration.instanceType' "$RESOURCE_FILE")

  if [ "$INSTANCE_TYPE" == "$EXPECTED_INSTANCE_TYPE" ]; then
    echo "Compliant: Instance type is $EXPECTED_INSTANCE_TYPE"
  else
    echo "Non-Compliant: Instance type is $INSTANCE_TYPE"
  fi

else
  echo "Resource configuration file not found."
fi
