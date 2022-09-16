# Introduction

Since Databricks is a third party application on Azure, it requires the additional role to read and write the data in the azure data lake storage.

## Add Storage Blob Data Contributor RBAC role to Resource Group

Once the app registration, app secret and enterprise application settings have been created/updated. You can assign RBAC role and assign it to the resource group. This will allow AzureDevOps to run it's pipelines for deployment.

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to Resource Groups.
3. Click on **rg-mdp-dev-01** resource group.  
   ![RG - Resource Group (select rg-mdp-dev-01)](./images/Resource%20Group%20(Select%20rg-mdp-dev-01).png).

4. Once the resource group page is loaded, click on the Access control (IAM) from the left side menu.  
   ![RG - Resource Group (Select Access Control (IAM) options)](./images/Resource%20Group%20(Select%20Access%20Control%20(IAM)%20option).png)

5. Once the Access Control (IAM) page is loaded click on the **Add Button** and then click on **Add role assignment**.  
   ![RG - Resource Group (Add Button)](./images/Resource%20Group%20(Access%20Control%20-%20Click%20Add%20Button).png)

6. Once the *Add role assignment* page is loaded, search for **Storage Blob Data Contributor**, then select the role and then click on the **Members** tab.  
   ![Azure - Access Control Add role assignment](./images/Azure%20-%20Access%20Control%20Add%20role%20assignment.png)

7. Once the *Members* tab is loaded, click on the **+ Select members** link; then find service principal *sp-mdp-dev-01* and then click on the **Select** button. Once the panel is closed, click on the **Review + Assign** button.  
  ![Azure - Access Control Add role assignment members](./images/Azure%20-%20Access%20Control%20Add%20role%20assignment%20members.png)  

8. Once the *Review + Assign* page loads, click on the **Review + assign** button.  
   ![Azure - Access Control Add role assignment review and assign](./images/Azure%20-%20Access%20Control%20Add%20role%20assignment%20review%20and%20assign.png)
