variable "access_key" {
  type        = string
  description = "access_key"
}


variable "secret_key" {
  type        = string
  description = "secret_key"
}

variable "name" {
  type        = string
  description = "DB_name"
  default = "postgres"
}

variable "username" {
  type        = string
  description = "DB_username"
  default = "postgres"
}

variable "password" {
  type        = string
  description = "DB_password"
}

