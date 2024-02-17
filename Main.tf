provider "aws" {
  region = "us-eastt-1"  # Choose your desired region
}

resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
}

# Additional resources like Subnets, Security Groups, etc.
