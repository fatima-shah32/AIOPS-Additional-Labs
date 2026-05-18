#!/bin/bash

echo "=============================="
echo " Installing Nginx"
echo "=============================="

# Update packages
sudo apt update -y

# Install nginx
sudo apt install nginx -y

# Enable nginx at boot
sudo systemctl enable nginx

# Start nginx
sudo systemctl start nginx

# Check status
sudo systemctl status nginx --no-pager

echo "Nginx installation completed successfully!"
