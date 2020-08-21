provider "aws" {
  region = "us-east-2"
  profile = "dockdesafio"
}

resource "aws_security_group" "block-dynamic-dockdesafio" {
  name        = "dockdesafio-sg"
  description = "Security Group com block dynamic"

  dynamic "ingress" {
    for_each = var.default_ingress
    content {
      description = ingress.value["description"]
      from_port   = ingress.key
      to_port     = ingress.key
      protocol    = "tcp"
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }

  tags = {
    Name = "dockdesafio"
  }
}

terraform {
  backend "s3" {
    bucket = "dockdesafio-tfstate"
    key    = "sg/terraform.state"
    region = "us-east-2"
    profile = "dockdesafio"
  }
}

output id {
  value = aws_security_group.block-dynamic-dockdesafio.id
}
