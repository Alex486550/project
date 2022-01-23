resource "aws_route_table" "route_table_kud" {
  vpc_id = aws_vpc.vpc_kud.id
  route {
    cidr_block     = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw_kud.id
  }
  tags = {
    Name = "route_table_kud"
  }
}

resource "aws_route_table" "route_table1_kud" {
  vpc_id = aws_vpc.vpc_kud.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat1_gateway_kud.id
  }
  tags = {
    Name = "route_table1_kud"
  }
}

resource "aws_route_table" "route_table2_kud" {
  vpc_id = aws_vpc.vpc_kud.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat2_gateway_kud.id
  }
  tags = {
    Name = "route_table2_kud"
  }
}
