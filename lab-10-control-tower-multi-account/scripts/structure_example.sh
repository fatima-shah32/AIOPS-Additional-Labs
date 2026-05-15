#!/bin/bash

echo "========================================="
echo "Simulating AWS Control Tower Landing Zone"
echo "========================================="

mkdir -p AWS_Accounts/Org_Unit_1/Account_1
mkdir -p AWS_Accounts/Org_Unit_1/Account_2
mkdir -p AWS_Accounts/Org_Unit_2/Account_3
mkdir -p AWS_Accounts/Root_Account

echo "Multi-account structure created successfully."
tree AWS_Accounts
