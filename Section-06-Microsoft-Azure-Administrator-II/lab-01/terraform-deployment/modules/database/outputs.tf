output "mysql_server_fqdn" {
  value = azurerm_mysql_flexible_server.main.fqdn
}

output "database_name" {
  value = azurerm_mysql_flexible_database.main.name
}
