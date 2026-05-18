provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "vm" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tags = {
    Name = "Lab9-Terraform-VM"
  }
}
