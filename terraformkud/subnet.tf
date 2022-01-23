resource "aws_subnet" "pub1_kud" {
  cidr_block              = "192.168.1.0/24"
  vpc_id                  = aws_vpc.vpc_kud.id
  availability_zone       = local.region1
  map_public_ip_on_launch = true
  tags = {
    Name                        = "pub1_kud"
    "kubernetes.io/cluster/eks" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}

resource "aws_subnet" "pub2_kud" {
  cidr_block              = "192.168.2.0/24"
  vpc_id                  = aws_vpc.vpc_kud.id
  availability_zone       = local.region2
  map_public_ip_on_launch = true
  tags = {
    Name                        = "pub2_kud"
    "kubernetes.io/cluster/eks" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}


resource "aws_subnet" "priv1_kud" {
  cidr_block        = "192.168.3.0/24"
  vpc_id            = aws_vpc.vpc_kud.id
  availability_zone = local.region1
  tags = {
    Name                              = "priv1_kud"
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "priv2_kud" {
  cidr_block        = "192.168.4.0/24"
  vpc_id            = aws_vpc.vpc_kud.id
  availability_zone = local.region2
  tags = {
    Name                              = "priv2_kud"
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}
