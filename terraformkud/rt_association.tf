resource "aws_route_table_association" "pub1_assoc_kud" {
  route_table_id = aws_route_table.route_table_kud.id
  subnet_id      = aws_subnet.pub1_kud.id
}

resource "aws_route_table_association" "pub2_assoc_kud" {
  route_table_id = aws_route_table.route_table_kud.id
  subnet_id      = aws_subnet.pub2_kud.id
}

resource "aws_route_table_association" "priv1_assoc_kud" {
  route_table_id = aws_route_table.route_table1_kud.id
  subnet_id      = aws_subnet.priv1_kud.id
}

resource "aws_route_table_association" "priv2_assoc_kud" {
  route_table_id = aws_route_table.route_table2_kud.id
  subnet_id      = aws_subnet.priv2_kud.id
}

