variable default_ingress {
  type = map(object({description = string, cidr_blocks = list(string)}))
  default = {
    22 = { description = "SSH", cidr_blocks = [ "127.0.0.1/32" ] }
    80 = { description = "HTTP", cidr_blocks = [ "127.0.0.1/32" ] }
    443 = { description = "HTTPS", cidr_blocks = [ "127.0.0.1/32" ] }
  }
}
