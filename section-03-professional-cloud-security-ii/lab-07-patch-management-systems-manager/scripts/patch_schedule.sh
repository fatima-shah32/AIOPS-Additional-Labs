#!/bin/bash

# Simulate Patch Scheduling

PATCHING_SCHEDULE="*/15 * * * *"
PATCH_SCRIPT="apply_patches.sh"

echo "========================================="
echo "Simulating Patch Scheduling"
echo "========================================="

echo "Setting patch schedule..."

echo "$PATCHING_SCHEDULE $PATCH_SCRIPT" >> my_cron_jobs.txt

echo ""
echo "Patch schedule added successfully."
echo "Schedule: Run $PATCH_SCRIPT every 15 minutes."
