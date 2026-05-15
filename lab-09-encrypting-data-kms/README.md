# Lab 9: Encrypting Data with AWS KMS

## Objective
Simulate AWS KMS customer master key (CMK) management and integrate encryption/decryption workflows similar to Amazon S3 encryption at rest.

---

## Tools Used
- Ubuntu Linux
- Bash scripting
- OpenSSL
- jq
- Simulated AWS KMS concepts

---

## Folder Structure

lab-09-encrypting-data-kms/
├── configs
├── reports
├── screenshots
└── scripts

---

## Configurations

### cmk_config.json
Defines a simulated AWS KMS customer master key.

---

## Scripts

### manage_cmk.sh
Simulates CMK management operations.

### encrypt_s3_object.sh
Simulates encrypting an S3 object using KMS.

### decrypt_s3_object.sh
Simulates decrypting an encrypted object using KMS.

---

## Outcome

Successfully simulated:
- AWS KMS CMK management
- Key rotation
- File encryption
- File decryption
- Secure storage workflows
