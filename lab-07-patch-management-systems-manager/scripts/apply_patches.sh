#!/bin/bash

# Simulate Applying Patch Baseline

PATCH_BASELINE_FILE="../configs/patch_baseline.json"

APPROVED_PATCHES=("ubuntu-20.04.5" "ubuntu-20.04.6")

echo "========================================="
echo "Simulating Patch Application"
echo "========================================="

echo "Using baseline file: $PATCH_BASELINE_FILE"

echo ""

for PATCH in "${APPROVED_PATCHES[@]}"; do
    echo "Applying patch: $PATCH"
    echo "$PATCH applied successfully."
    echo ""
done

echo "Patch application completed successfully."
