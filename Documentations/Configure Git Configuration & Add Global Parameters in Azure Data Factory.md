# Introduction

Once the ARM template for the data factory is deployed, it required Git integration for any changes made during development. Lastly, the global variables are commonly used name throughout the ADF framework pipeline.

## Configure Git Configuration & Add Global Parameters in Azure Data Factory

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to Resource Groups.
3. Click on **rg-mdp-dev-01** resource group.  
   ![RG - Resource Group (select rg-mdp-dev-01)](./images/Resource%20Group%20(Select%20rg-mdp-dev-01).png).

4. Once the *Resource group* page loads, click on the **Azure Data Factory** resource.  
   ![Azure - Resource group Azure Data Factory](./images/Azure%20-%20Resource%20group%20Azure%20Data%20Factory.png)

5. Once the *Azure data factory* overview page is loaded, click on the **Open Azure Data Factory Studio** link.  
   ![Azure - Azure Data Factory Open](./images/Azure%20-%20Azure%20Data%20Factory%20Open.png)

6. Once the *Azure Data Factory* home page opens, click on the Manage option from the left side menu.  
   ![Azure - Azure Data Factory Home Page Manage](./images/Azure%20-%20Azure%20Data%20Factory%20Home%20Page%20Manage.png)  

7. The *Manage* page will open to *Link services* page, on the left side menu, click on the **Git configuration** option.  
   ![Azure - Azure Data Factory Git configuration](./images/Azure%20-%20Azure%20Data%20Factory%20Git%20configuration.png)  

8. Once the *Git configuration* page is loaded, click on the **configure** button.  
   ![Azure - Azure Data Factory Git configure button](./images/Azure%20-%20Azure%20Data%20Factory%20Git%20configure%20button.png)

9. Once the *Configure a repository* blade appears, from the *Repository type* dropdown menu, select *Azure DevOps Git* from the *Azure Active Directory* select your relevant Azure Tenant and then click on the **Continue** button.  
   ![Azure - Azure Data Factory Configure a repository](./images/Azure%20-%20Azure%20Data%20Factory%20Configure%20a%20repository.png)

10. The next blade will appear for selecting and linking a repository.  
    When the *Select option* is selected, select the following the drop down menu and then click on the **Save** button.  
    ![Azure - Azure Data Factory Configure a repository Select repository](./images/Azure%20-%20Azure%20Data%20Factory%20Configure%20a%20repository%20Select%20respository.png)  

11. After clicking the *Apply* button the **Set working branch** will appear. Click the **Save** button.  
    ![Azure Data Factory Set working branch](./images/Azure%20Data%20Factory%20Set%20working%20branch.png)

## Adding global parameters

After clicking the *Save button*, you will return back to the *Configure a repository* page. You will need to add 2 global parameters which is used by the ADF pipeline.  

1. Click on the **Global parameters* option on the left side menu.  
    ![Azure Data Factory Configure a repository with git configuration](./images/Azure%20Data%20Factory%20Configure%20a%20repository%20with%20git%20configuration.png)

2. Once the *Global parameters* page is loaded, click on the **+ New** button. Once the *New global parameter* blade appears, enter the following in the screenshot below and then click on the **Save** button.  
   ![Azure Data Factory Global parameters keyVaultName](./images/Azure%20Data%20Factory%20Global%20parameters%20keyVaultName.png)

3. Repeat step 2 and add a parameter for `storageName` and with the value of the Azure Storage blob name.  
   ![Azure Data Factory Global parameters storageName](./images/Azure%20Data%20Factory%20Global%20parameters%20storageName.png)

## Validating your configurations

After adding the Git configuration & Global parameters, click on the **Validate all** button to ensure there is no issues or missing configurations. The **Factory validation output** blade will appear and there should no validation errors. Click on the **Close** button afterwards.  
   ![Azure Data Factory Validate All](./images/Azure%20Data%20Factory%20Validate%20All.png)

## Upload ARM Template for Data Factory

Once the validation is completed. The next step is to upload the arm template to populate pipelines and databases. You will need to first log into Azure DevOps and download the `ARMTemplateForFactory.json` file.

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Once the *Azure DevOps* home page is loaded, hover over and click the **repo** icon.  
   ![Azure DevOps Homepage](./images/Azure%20DevOps%20Homepage.gif)

3. Go to **Pipelines > Pipelines**. Once the *Pipelines* page is open, click on the successful **MDP-Framework** pipeline.
   ![Azure DevOps Pipelines MDP-Framework](./images/Azure%20DevOps%20Pipelines%20MDP-Framework.png)

4. Once the *MDP-Framework Runs* page and tab is loaded, click on the **successful run**.  
   ![Azure DevOps Pipelines Runs](./images/Azure%20DevOps%20Pipelines%20Runs.png)

5. Once *Run* page is loaded, click on the **Windows** row in the **Jobs** section.  
   ![Azure DevOps Pipelines Runs Jobs](./images/Azure%20DevOps%20Pipelines%20Runs%20Jobs.png)

6. Once the *Jobs -> Windows* page is loaded, click on the **4 artifacts** provided.  
   ![Azure DevOps Jobs Windows](./images/Azure%20DevOps%20Jobs%20Windows.png)

7. Once the artifact page is loaded, click on the ellipsis for the **ADF Artifact** and then click on the **Download Artifacts**.  
   ![Azure DevOps ADF Artifact](./images/Azure%20DevOps%20Download%20ADF%20Artifacts.png)

8. The ADF Artifacts will be downloaded as a zip file. Extract the zip file.  
   ![Windows ADF Artifact Downloaded](./images/Windows%20ADF%20Artifact%20Downloaded.png)

9. Once you have downloaded the `ARMTemplateForFactory.json`, log into the [Azure Portal](https://portal.azure.com/)
10. Go to Resource Groups.
11. Once the *Resource group* page loads, click on the **Azure Data Factory** resource.  
   ![Azure - Resource group Azure Data Factory](./images/Azure%20-%20Resource%20group%20Azure%20Data%20Factory.png)

12. Once the *Azure data factory* overview page is loaded, click on the **Open Azure Data Factory Studio** link.  
   ![Azure - Azure Data Factory Open](./images/Azure%20-%20Azure%20Data%20Factory%20Open.png)

13. Once the *Azure Data Factory* home page opens, click on the Manage option from the left side menu.  
   ![Azure - Azure Data Factory Home Page Manage](./images/Azure%20-%20Azure%20Data%20Factory%20Home%20Page%20Manage.png)  

14. Once the *Manage* page is loaded, click on the **ARM template** label on the left side menu. Once the *Arm Template* page appears, click on the **Import ARM template** button.  
   ![Azure Data Factory - ARM Template](./images/Azure%20Data%20Factory%20-%20ARM%20Template.png)

15. This will open a new page tab on your browser, once the *Custom deployment* page is loaded, click on the **Build your own template in the editor** link.  
   ![Azure - Custom deployment](./images/Azure%20-%20Custom%20deployment.png)

16. Once the *Edit template* button appears, click on the **Load file button**. Once the file dialog appears, select your file and click the **Open** button. Once the file is loaded in the editor section, click the **Save** button.  
   ![Azure - Edit template upload file](./images/Azure%20-%20Edit%20template%20upload%20file.png)

17. Once the *Custom deployment - Deploy from a custom template* page is loaded, select your resource group of where resources for the MDP framework is deployed and then following parameters are required to be changed.  

    |Parameter Name                                                |Parameter Value                      |
    |--------------------------------------------------------------|-------------------------------------|
    |Factory Name                                                  |Resource name of Azure Data Factory  |
    |Azure Data Lake Storage_properties_type Properties_url        |URL of Azure Storage Account Resource|
    |Azure Key Vault_properties_type Properties_base Url           |URL of Azure Key vault               |
    |Data Factory_properties_global Parameters_storage Name_value  |Name of Storage Account Resource     |
    |Data Factory_properties_global Parameters_key Vault Name_value|Name of Azure Key Vault Resource     |  

   ![Azure - Custom Deployment - Deploy from a custom template](./images/Azure%20-%20Custom%20Deployment%20-%20Deploy%20from%20a%20custom%20template.gif)  

18. Click the **Review + create** button.  
    ![Azure - Custom Deployment - Deploy from a custom template Review + Create](./images/Azure%20-%20Custom%20Deployment%20-%20Deploy%20from%20a%20custom%20template%20Review%20and%20create.png)

19. Once the ARM template is imported, click on the **Author** label on the left side menu, then click on the expand button to view all the Pipelines and Datasets created.  
   ![Azure Data Factory - Author](./images/Azure%20Data%20Factory%20-%20Author.gif)
