variable "resource_group_name" {
  default = "rg-terraform-lab"
}

variable "location" {
  default = "East US"
}

variable "environment" {
  default = "development"
}

variable "app_name" {
  default = "myterraformapp"
}

variable "admin_username" {
  default = "azureuser"
}

variable "vm_size" {
  default = "Standard_B1s"
}
