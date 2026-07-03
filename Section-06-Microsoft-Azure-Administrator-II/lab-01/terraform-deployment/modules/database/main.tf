resource "azurerm_mysql_flexible_server" "main" {
  name                   = "${var.app_name}-mysql"
  resource_group_name    = var.resource_group_name
  location               = var.location
  administrator_login    = var.admin_username
  administrator_password = "P@ssw0rd123!"

  sku_name = "B_Standard_B1s"
  version  = "8.0.21"

  storage {
    size_gb = 20
  }
}

resource "azurerm_mysql_flexible_database" "main" {
  name                = "${var.app_name}db"
  resource_group_name = var.resource_group_name
  server_name         = azurerm_mysql_flexible_server.main.name
  charset             = "utf8"
  collation           = "utf8_unicode_ci"
}
