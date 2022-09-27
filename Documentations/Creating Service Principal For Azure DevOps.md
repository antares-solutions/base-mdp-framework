# Creating a Service Principal

Service principals (App Registrations) is created under Azure Active Directory and requires RBAC access to the responding resource groups.

|Name convention|Resource Group|Role       |
|---------------|--------------|-----------|
|sp-mdp-dev-01  |rg-mdp-dev-01 |Contributor|

Please see below steps for creating a service principal.  

1. Log into [Azure Portal](https://portal.azure.com/)
2. Go to Azure Active Directory.
3. Select App Registration from the left hand-side.  
   ![AAD - App Registration](./images/Azure%20Active%20Directory%20(App%20Registration).PNG)

4. Click on the **New Registration** button.  
   ![AAD - App Registration](./images/App%20Registration%20(New%20Registration).PNG)

5. Enter the user-facing display name *sp-mdp-dev-01* and select **Accounts in this organizational directory only (Default Directory only - Single tenant)**. In the Redirect URI section select **Single-page application** and the URL `https://VisualStudio/SPN/` into the text box; and then click the register button.  
   ![AAD - App Registration (Register An Application)](./images/App%20Registration%20(Register%20An%20Application).PNG)

6. Once the app registration is completed, from the left side menu select **Authentication**.  
   ![ADD - App Registration (Select Authentication)](./images/App%20Registration%20(Select%20Authentication).png)

7. Once the authentication page, is loaded, under the **Implicit grant and hybrid flows**; check the **ID Tokens (used for implicit flows)**. And then click the Save button.  
   ![ADD - App Registration (ID Tokens)](./images/App%20Registration%20(Check%20ID%20tokens).png)


## Creating an app secret

Once all the app registration is created, you need to create an app secret which will be used when deploying when setting up the repository in Azure DevOps.

Please see steps below for creating the app secret.

1. Log into [Azure Portal](https://portal.azure.com/)
2. Go to Azure Active Directory.
3. Select App Registration from the left hand-side.  
   ![AAD - App Registration](./images/Azure%20Active%20Directory%20(App%20Registration).PNG)

4. Click on the app applications tab (if you did not create the app registration).  
   ![ADD - App Registration(Select All Application tab)](./images/App%20Registration%20(Select%20All%20Applications).PNG)

5. Click on the app registration *sp-mdp-dev-01*.  
   ![ADD - App Registration (Select sp-mdp-dev-01 app registration)](./images/App%20Registration%20(Select%20sp-mdp-dev-01).png)

6. Once the app registration page is loaded for *sp-mdp-dev-01*, on the left side menu, select **Certificates & Secrets**.  
   ![ADD - App Registration (Certificates & Secrets)](./images/App%20Registration%20(Certificates%20%26%20Secrets).png)

7. Once the **Certificates and Secrets** page is loaded, click on the **New client secret** button. Enter the description and click on the **Add** button.  
   ![ADD - App Registration (Creating app secret)](./images/App%20Registration%20(Creating%20app%20secret).png)

8. Once the secret is created, copy the value of the secret, you will need it for when setting up the repository in Azure DevOps.  
   ![ADD - App Registration (Copying the app secret)](./images/App%20Registration%20(copy%20the%20secret%20value).png)


## Enterprise application settings

The following settings are required in the Enterprise application for the created App Registrations.

1. Log into [Azure Portal](https://portal.azure.com/)
2. Go to Azure Active Directory.
3. Select Enterprise application on the left side menu.  
   ![ADD - Enterprise Applications](./images/Enterprise%20Applications.png)

4. Click on application *sp-mdp-dev-01*.  
   ![ADD - Enterprise Applications(Select sp-mdp-dev-01)](./images/Enterprise%20Application%20(Select%20sp-mdp-dev-01).png)

5. Once the application page is loaded, on the left side menu select **Properties**.  
   ![ADD - Enterprise Applications (sp-mdp-dev-01 properties)](./images/Enterprise%20Properties%20(sp-mdp-dev-01%20Properties).png)

6. Once the properties page is loaded, set **Visible to users** to *Yes* and then click on the **Save** button.  
   ![ADD - Enterprise Applications (sp-mdp-dev-01 properties - Set Visble to users option)](./images/Enterprise%20applications%20(Properties%20for%20sp-mdp-dev-01%20-%20Set%20Visible%20to%20users).png)

## Assign RBAC role to service principal against subscription

Once the app registration is completed, you will assign the service principal(s) that have you created against the subscription.

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to your subscription is created. Once the *Subscription* page is loaded, from the left side menu click on **Access Control (IAM)** link.  
   ![Azure Subscription (Access control (IAM))](./images/Azure%20Subscription%20(Access%20control%20(IAM)).png)

3. Once the *Access Control (IAM)) page is loaded, click on the **Add** button and then click on the **Add role assignment** option.  
   ![Azure Subscription (Add role assignment)](./images/Azure%20Subscription%20(Add%20role%20assignment).png)

4. Once the *Add role assignment* page is loaded, click on the **Contributor** from the **Role** and then click on the Members tab.  
   ![Azure Subscription (Select Contributor role)](./images/Azure%20Subscription%20(Select%20Contributor%20role).png)

5. Once the *Members* tab is loaded, click on the **Select members** link and when **Select members** blade appears search and add your service principal and then click on the **Select** button and click on the **Review + assign** button.  
   ![Azure Subscription (Select Members)](./images/Azure%20Subscription%20(Select%20Members).gif)

6. Once the *Review + assign* page appears, click on the **Review + Assign** button.
   ![Azure Subscription(Review + assign)](./images/Azure%20Subscription(Review%20%2B%20assign).png)


## Assign Access and role to service principal against resource group

Once the app registration, app secret and enterprise application settings have been created/updated. You can assign RBAC role and assign it to the resource group. This will allow AzureDevOps to run it's pipelines for deployment.

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to Resource Groups.
3. Click on **rg-mdp-dev-01** resource group.  
   ![RG - Resource Group (select rg-mdp-dev-01)](./images/Resource%20Group%20(Select%20rg-mdp-dev-01).png).

4. Once the resource group page is loaded, click on the Access control (IAM) from the left side menu.  
   ![RG - Resource Group (Select Access Control (IAM) options)](./images/Resource%20Group%20(Select%20Access%20Control%20(IAM)%20option).png)

5. Once the Access Control (IAM) page is loaded click on the **Add Button** and then click on **Add role assignment**.  
   ![RG - Resource Group (Add Button)](./images/Resource%20Group%20(Access%20Control%20-%20Click%20Add%20Button).png)

6. Once the **Add role assignment** page is open, select the *Contributor* option and click on the **Members** tab.
   ![RG - Resource Group (Select Contributor role)](./images/Resource%20Group%20(Select%20Contributor%20Role).png)

7. Once the **Members** tab is loaded, click on the **Select members** link. Once the **Select Members** blade appears in the **Select** search box search for *sp-mdp-dev-01* service principal and then select it then click on the **Select** button.  
   ![RG - Resource Group (Add sp-mdp-dev-01 as member)](./images/Resource%20Group%20(Add%20sp-mdp-dev-01%20as%20member).png)

8. Click on the Review and Assign tab and then click on the **Review + assign** button.
   ![RG - Resource Group (Review and Assign Role)](./images/Resource%20Group%20(Review%20and%20Assign).png)

