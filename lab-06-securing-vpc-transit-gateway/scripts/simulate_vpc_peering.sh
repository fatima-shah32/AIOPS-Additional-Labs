#!/bin/bash

# Simulate VPC Peering Connection

VPC1_CIDR="10.0.0.0/16"
VPC2_CIDR="192.168.0.0/16"

echo "======================================="
echo "Simulating VPC Peering Connection"
echo "======================================="

echo "VPC 1 CIDR: $VPC1_CIDR"
echo "VPC 2 CIDR: $VPC2_CIDR"

echo ""
echo "Allowing traffic between VPCs..."

echo "Traffic allowed from $VPC1_CIDR to $VPC2_CIDR"
echo "Traffic allowed from $VPC2_CIDR to $VPC1_CIDR"

echo ""
echo "VPC Peering Simulation Completed Successfully"
