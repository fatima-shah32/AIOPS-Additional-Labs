#!/bin/bash

# Simulate Encrypting an S3 Object with AWS KMS

FILE_NAME="data_object.txt"
ENCRYPTED_FILE="data_object_encrypted.txt"
CMK_KEY="cmk-1234567890"

echo "========================================="
echo "Simulating S3 Object Encryption"
echo "========================================="

# Create sample file
echo "This is a sample file for encryption." > "$FILE_NAME"

echo ""
echo "Original File Content:"
cat "$FILE_NAME"

echo ""
echo "Encrypting file using simulated CMK..."

openssl enc -aes-256-cbc -salt \
-in "$FILE_NAME" \
-out "$ENCRYPTED_FILE" \
-pass pass:"$CMK_KEY"

echo "File encrypted successfully."

echo ""
echo "Encrypted File Content (Base64):"
base64 "$ENCRYPTED_FILE"
