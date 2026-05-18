#!/bin/bash

echo "============================"
echo " Creating Multiple Users"
echo "============================"

users=("user1" "user2" "user3")

for user in "${users[@]}"; do

  # Create user with home directory
  sudo useradd -m "$user"

  # Set password
  echo "$user:password123" | sudo chpasswd

  echo "User $user created successfully!"
done

echo "All users created."
