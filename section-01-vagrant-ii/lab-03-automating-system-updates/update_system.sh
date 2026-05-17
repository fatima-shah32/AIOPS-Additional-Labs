#!/bin/bash

echo "Updating package lists..."
sudo apt update -y

echo "Upgrading installed packages..."
sudo apt upgrade -y

echo "Removing unnecessary packages..."
sudo apt autoremove -y

echo "Cleaning package cache..."
sudo apt clean

echo "System updated successfully!"
