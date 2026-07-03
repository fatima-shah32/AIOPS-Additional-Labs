output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "public_ip_address" {
  value = module.compute.public_ip_address
}

output "mysql_server_fqdn" {
  value = module.database.mysql_server_fqdn
}

output "database_name" {
  value = module.database.database_name
}

output "application_url" {
  value = "http://${module.compute.public_ip_address}"
}
