#!/bin/bash

echo "===================================="
echo " LAB 5 - Static IP Configuration"
echo "===================================="

# Detect interface automatically
interface=$(ip route | grep default | awk '{print $5}')

echo "Detected Interface: $interface"

# Static IP details (demo values)
ip_address="192.168.1.100"
netmask="255.255.255.0"
gateway="192.168.1.1"
dns="8.8.8.8"

echo ""
echo "Applying Static IP Configuration (SIMULATION MODE)"
echo "IP Address: $ip_address"
echo "Netmask: $netmask"
echo "Gateway: $gateway"
echo "DNS: $dns"

echo ""
echo "NOTE:"
echo "On AWS cloud systems, network is managed automatically (DHCP)."
echo "So we are only simulating configuration for lab learning."
