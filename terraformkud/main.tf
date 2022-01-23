provider "aws" {
  region = local.region
  access_key = var.access_key
  secret_key = var.secret_key

}

locals {
  name   = "kud-postgresql"
  region = "eu-central-1"
  region1 = "eu-central-1a"
  region2 = "eu-central-1b"
  tags = {
    Owner       = "Aleksandr_Kudeenko@epam.com"
    Environment = "dev"
  }
}

