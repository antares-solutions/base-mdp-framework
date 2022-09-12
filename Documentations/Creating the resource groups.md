# Creating resource groups

Resource groups must be created before deploying the MDP solution. For more information see [Manage Azure resource groups by using the Azure portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) for more info.

For the MDP framework, three resource group is required:

|Naming Convention|Environment|
|-----------------|-----------|
|mdp-dev-01       |DEV        |

## Create Resource Group via CLI

Resource group can also be created via Azure CLI.

1. Sign in and open the Azure Bash Terminal.
2. If required, change to your relevant tenant with `azlogin --tenant <myTenantID>`
3. If required, change to your relevant subscription with`az account set --subscription "<Subscription Name or Subscription Id>"`.
4. To create the resource group, run `az group create --name <resource-Name> --location <location>`.
5.To verify that the resource group is created in Azure run `az group show --name <exampleGroup>`.


## Create Resource Group via Azure Portal

1. Log into [Azure Portal](https://portal.azure.com/)
2. Go to Resource Groups.
3. Click on the **Create** button.  
   ![RG - Resource Group (Create Resource Group)](./images/Resource%20Group%20(Create%20RG).png)

4. Once the **Create a resource group** page is loaded, select your subscription, Enter resource group name *rg-mdp-dev-01* and select appropriate region. Lastly, click on the **Review + create** button.  
  ![RG - Resource Group (Enter Details)](./images/Resource%20Group%20(Enter%20Details).png)

5. Once the **Review + create** tab is loaded. Click on the **Create button**.  
   ![RG - Resource Group (Create)](./images/Resource%20Group%20(Create%20RG).png)