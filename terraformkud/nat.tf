resource "aws_nat_gateway" "nat1_gateway_kud" {
  allocation_id = aws_eip.eip1_kud.id
  subnet_id     = aws_subnet.pub1_kud.id
  tags = {
    Name = "nat1_gateway_kud"
  }
}

resource "aws_nat_gateway" "nat2_gateway_kud" {
  allocation_id = aws_eip.eip2_kud.id
  subnet_id     = aws_subnet.pub2_kud.id
  tags = {
    Name = "nat2_gateway_kud"
  }
}
