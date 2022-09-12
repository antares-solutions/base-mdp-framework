# Introduction

Registering resource providers (namespaces) is required for a successful deployment of the MDP framework from Azure DevOps. Please see list below for namespaces that are required for the MDP Framework.  

|Namespace            |Description          |
|---------------------|---------------------|
|Microsoft.Sql        |Azure SQL Database   |
|Microsoft.DataFactory|Azure Data Factory   |
|Microsoft.Databricks |Azure Databricks     |
|Microsoft.Storage    |Azure Storage Account|
|Microsoft.KeyVault   |Azure Key Vault      |

## How to register resource providers

1. Log into the [Azure Portal](https://portal.azure.com/).
2. Go to Subscriptions and then your subscription where the MDP framework will be deployed. Once the *Subscriptions* page is loaded, click on the **Resource providers** label.
   ![Azure - Subscriptions](./images/Azure%20-%20Subscriptions.png)  

3. Once the *Resource providers* page is loaded, enter the resource name listed above, click on the searched provider and then click on the register button.  
   ![Azure - Subscriptions - Resources](./images/Azure%20-%20Subscriptions%20-%20Resources.png)

4. Repeat steps 2 to 3 for registering the other namespace providers.
