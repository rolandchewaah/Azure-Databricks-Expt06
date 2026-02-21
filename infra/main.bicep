// infra/main.bicep
param location string = resourceGroup().location
param workspaceName string = 'dbw-ingestion-dev'
param storageAccountName string = 'stlakehousedev'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
  properties: { isHnsEnabled: true } // Enabled for ADLS Gen2
}

resource databricksWorkspace 'Microsoft.Databricks/workspaces@2023-02-01' = {
  name: workspaceName
  location: location
  sku: { name: 'premium' } // Premium required for Unity Catalog/Service Principals
}