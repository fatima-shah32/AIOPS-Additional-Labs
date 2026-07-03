#!/bin/bash

echo "=== Terraform Multi-Tier Application Deployment ==="

echo "Initializing Terraform..."
terraform init

echo "Validating Terraform configuration..."
terraform validate

echo "Planning Terraform deployment..."
terraform plan -out=tfplan

echo ""
echo "Plan Summary:"
echo "Resource Group: rg-terraform-lab"
echo "Virtual Network with web, app, and db subnets"
echo "Load Balancer with Public IP"
echo "MySQL Flexible Server"
echo ""
echo "To deploy for real, run:"
echo "terraform apply tfplan"
