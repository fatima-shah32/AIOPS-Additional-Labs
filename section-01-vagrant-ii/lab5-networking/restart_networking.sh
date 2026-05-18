#!/bin/bash

echo "===================================="
echo " Restarting Networking Services"
echo "===================================="

sudo systemctl restart networking

echo "Networking restarted successfully!"
