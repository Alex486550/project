resource "aws_internet_gateway" "igw_kud" {
  vpc_id = aws_vpc.vpc_kud.id
  tags = {
    Name = "igw_kud"
  }
}

resource "aws_eip" "eip1_kud" {
}

resource "aws_eip" "eip2_kud" {
}
