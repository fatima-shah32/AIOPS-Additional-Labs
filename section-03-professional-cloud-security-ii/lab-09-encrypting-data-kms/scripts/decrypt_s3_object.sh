#!/bin/bash

# Simulate Decrypting an S3 Object with AWS KMS

ENCRYPTED_FILE="data_object_encrypted.txt"
DECRYPTED_FILE="data_object_decrypted.txt"
CMK_KEY="cmk-1234567890"

echo "========================================="
echo "Simulating S3 Object Decryption"
echo "========================================="

echo ""
echo "Decrypting file using simulated CMK..."

openssl enc -d -aes-256-cbc \
-in "$ENCRYPTED_FILE" \
-out "$DECRYPTED_FILE" \
-pass pass:"$CMK_KEY"

echo "File decrypted successfully."

echo ""
echo "Decrypted File Content:"
cat "$DECRYPTED_FILE"
