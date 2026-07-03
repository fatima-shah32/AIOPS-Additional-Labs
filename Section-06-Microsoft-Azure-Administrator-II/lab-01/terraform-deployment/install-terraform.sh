#!/bin/bash

echo "Installing Terraform..."

TERRAFORM_VERSION="1.6.0"

wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip

sudo apt update
sudo apt install -y unzip

unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip

sudo mv terraform /usr/local/bin/

terraform version

rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

echo "Terraform installation completed."
