#!/bin/bash

# Simulate AWS Transit Gateway

echo "======================================="
echo "Simulating AWS Transit Gateway"
echo "======================================="

VPC1_CIDR="10.0.0.0/16"
VPC2_CIDR="192.168.0.0/16"

echo "Transit Gateway routing enabled"

echo ""
echo "Routing traffic between VPCs..."

echo "Allow traffic from $VPC1_CIDR to $VPC2_CIDR"
echo "Allow traffic from $VPC2_CIDR to $VPC1_CIDR"

echo ""
echo "Transit Gateway Simulation Completed Successfully"
