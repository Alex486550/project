resource "aws_vpc" "vpc_kud" {
  cidr_block                       = "192.168.0.0/16"
  enable_dns_hostnames             = true
  enable_dns_support               = true
  instance_tenancy                 = "default"
  tags = {
    Name = "vpc_kud"
  }
}
