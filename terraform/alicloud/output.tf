output "public_ip" {
  value = alicloud_eip_address.eip.ip_address
}
