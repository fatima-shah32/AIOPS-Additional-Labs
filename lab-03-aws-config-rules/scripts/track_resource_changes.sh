#!/bin/bash

RESOURCE_FILE="../configs/mock_ec2_instance.json"

echo "Simulating AWS Config resource tracking..."

if [ -f "$RESOURCE_FILE" ]; then
  echo "Resource configuration tracked:"
  cat "$RESOURCE_FILE"
else
  echo "No resource configuration file found."
fi
