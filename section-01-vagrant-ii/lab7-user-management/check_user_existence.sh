#!/bin/bash

echo "============================"
echo " User Existence Checker"
echo "============================"

read -p "Enter username to check: " username

if id "$username" &>/dev/null; then
  echo "User $username exists!"
else
  echo "User $username does not exist!"
fi

