terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.24"
    }
  }
  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

variable "mode" {
  type        = string
  default     = "dev"
  description = "Instance name e.g. 'dev', 'prod', 'test'."
}
variable "image_name" {
  description = "Full path of the Docker image for the web application."
  nullable    = false
}
variable "image_tag" {
  description = "Tag of the Docker image for the web application."
  nullable    = false
}
variable "email_password" {
  sensitive   = true
  description = "Password for the rcsazbot role account."
  nullable    = false
}
variable "admin_password" {
  sensitive   = true
  description = "A secure password for the Django admin user."
  nullable    = false
}
# REVIEW - add any additional secrets/changing config settings as variables

locals {
  project_name           = "liionsden"                     # REVIEW
  location               = "ukwest"                        # REVIEW - the azure region to deploy into - https://github.com/claranet/terraform-azurerm-regions/blob/master/REGIONS.md
  django_settings_module = "liionsden.settings.production" # REVIEW - import path for project's azure settings
  postgres_admin_login   = "postgres"
  email_user             = "rcsazbot"
}

resource "azurerm_resource_group" "rg" {
  name     = "${local.project_name}-${var.mode}-rg"
  location = local.location
}

# Networking
resource "azurerm_virtual_network" "vnet" {
  name                = "${local.project_name}-${var.mode}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = local.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "db" {
  name                 = "${local.project_name}-${var.mode}-db-subnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.2.0/24"]
  service_endpoints    = ["Microsoft.Storage"]

  delegation {
    name = "fs"
    service_delegation {
      name    = "Microsoft.DBforPostgreSQL/flexibleServers"
      actions = ["Microsoft.Network/virtualNetworks/subnets/join/action"]
    }
  }
}

resource "azurerm_subnet" "app" {
  name                 = "${local.project_name}-${var.mode}-app-subnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
  service_endpoints    = ["Microsoft.Web", "Microsoft.Storage"]

  delegation {
    name = "webapp"
    service_delegation {
      name    = "Microsoft.Web/serverFarms"
      actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
    }
  }
}

resource "azurerm_private_dns_zone" "db" {
  name                = "${var.mode}.${local.project_name}.postgres.database.azure.com"
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_private_dns_zone_virtual_network_link" "db" {
  name                  = "${local.project_name}-${var.mode}-database-link"
  private_dns_zone_name = azurerm_private_dns_zone.db.name
  virtual_network_id    = azurerm_virtual_network.vnet.id
  resource_group_name   = azurerm_resource_group.rg.name
}

# Database
resource "random_password" "db" {
  length  = 24
  special = true
}

resource "azurerm_postgresql_flexible_server" "server" {
  name                   = "${local.project_name}-${var.mode}-db"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = local.location
  version                = "13" # REVIEW - postgres version - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_flexible_server#version
  delegated_subnet_id    = azurerm_subnet.db.id
  private_dns_zone_id    = azurerm_private_dns_zone.db.id
  administrator_login    = local.postgres_admin_login
  administrator_password = random_password.db.result
  storage_mb             = 2097152           # REVIEW - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_flexible_server#storage_mb
  sku_name               = "B_Standard_B1ms" # REVIEW - see https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-compute-storage#compute-tiers-vcores-and-server-types
  depends_on             = [azurerm_private_dns_zone_virtual_network_link.db]
}

resource "azurerm_postgresql_flexible_server_database" "db" {
  name      = local.project_name
  server_id = azurerm_postgresql_flexible_server.server.id
  charset   = "UTF8"
  collation = "en_US.utf8"
}

# File storage
resource "azurerm_storage_account" "media" {
  name                      = "${local.project_name}${var.mode}media"
  resource_group_name       = azurerm_resource_group.rg.name
  location                  = local.location
  account_tier              = "Standard" # REVIEW - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account#account_tier
  account_replication_type  = "LRS"      # REVIEW - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account#account_replication_type
  access_tier               = "Hot"      # REVIEW - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account#access_tier
  enable_https_traffic_only = true
  min_tls_version           = "TLS1_2"
}

resource "azurerm_storage_container" "media" {
  name                  = "media"
  storage_account_name  = azurerm_storage_account.media.name
  container_access_type = "private"
}

# Web application
resource "random_password" "secret_key" {
  length = 50
}

resource "azurerm_service_plan" "plan" {
  name                = "${local.project_name}-${var.mode}-plan"
  location            = local.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1" # REVIEW - https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/service_plan#sku_name
}

resource "azurerm_linux_web_app" "app" {
  name                      = "${local.project_name}-${var.mode}-app"
  resource_group_name       = azurerm_resource_group.rg.name
  location                  = local.location
  service_plan_id           = azurerm_service_plan.plan.id
  virtual_network_subnet_id = azurerm_subnet.app.id
  https_only                = true
  site_config {
    application_stack {
      docker_image     = var.image_name
      docker_image_tag = var.image_tag
    }
    health_check_path                 = "/" # REVIEW - a url path that will return a 200 response
    health_check_eviction_time_in_min = "2"
  }
  app_settings = {
    # REVIEW - add any extra environment variables for the web app here, these may need to be setup as Terraform variables above
    POSTGRES_HOST                   = azurerm_postgresql_flexible_server.server.fqdn
    POSTGRES_USER                   = local.postgres_admin_login
    POSTGRES_PASSWORD               = random_password.db.result
    POSTGRES_NAME                   = azurerm_postgresql_flexible_server_database.db.name
    DJANGO_SETTINGS_MODULE          = local.django_settings_module
    SECRET_KEY                      = random_password.secret_key.result
    WEBSITES_PORT                   = 8000
    EMAIL_USER                      = local.email_user
    EMAIL_PASSWORD                  = var.email_password
    ADMIN_PASSWORD                  = var.admin_password
    AZURE_STORAGE_CONTAINER         = azurerm_storage_container.media.name
    AZURE_STORAGE_CONNECTION_STRING = azurerm_storage_account.media.primary_connection_string
    AZURE_ACCOUNT_NAME              = azurerm_storage_account.media.name
  }
  logs {
    http_logs {
      file_system {
        retention_in_days = 0
        retention_in_mb   = 35
      }
    }
  }
}

# Web application logging
resource "azurerm_log_analytics_workspace" "app" {
  name                = "${local.project_name}-${var.mode}-analytics"
  location            = local.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 90
}

resource "azurerm_monitor_diagnostic_setting" "app" {
  name                           = "${local.project_name}-${var.mode}-logging"
  target_resource_id             = azurerm_linux_web_app.app.id
  log_analytics_workspace_id     = azurerm_log_analytics_workspace.app.id
  log_analytics_destination_type = "Dedicated"
  log {
    category = "AppServiceHTTPLogs"
    enabled  = true
    retention_policy {
      enabled = false
    }
  }
  log {
    category = "AppServiceConsoleLogs"
    enabled  = true
    retention_policy {
      enabled = false
    }
  }
  metric {
    category = "AllMetrics"

    retention_policy {
      enabled = false
    }
  }
}
