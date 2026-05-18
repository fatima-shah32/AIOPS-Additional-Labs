#!/bin/bash

echo "============================"
echo " Deleting Users"
echo "============================"

users=("user1" "user2" "user3")

for user in "${users[@]}"; do

  if id "$user" &>/dev/null; then
    sudo userdel -r "$user"
    echo "User $user deleted successfully!"
  else
    echo "User $user does not exist!"
  fi

done

echo "Deletion process completed."
