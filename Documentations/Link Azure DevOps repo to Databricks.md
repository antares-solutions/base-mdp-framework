# Introduction

The purpose of linking the Azure DevOps to Databricks is to link the Databricks notebooks from the repository. You will need the repository link from Azure DevOps before continuing.

## Copy Azure DevOps Repository Link

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Once the *Azure DevOps* home page is loaded, hover over and click the **repo** icon.  
   ![Azure DevOps Homepage](./images/Azure%20DevOps%20Homepage.gif)

3. Once the repository page is open, click on the **Clone** button.  
   ![Azure DevOps Repository](./images/Azure%20DevOps%20Repository.png)

4. Once the *Clone Repository* page is loaded, click on the copy button.  
   ![Azure DevOps Clone Repository](./images/Azure%20DevOps%20Clone%20Repository.png)

## Link Azure DevOps repo to Databricks

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the databricks home page is loaded, open the left side menu bar and then click on **Repos**. Once the *Repos* blade is open, click on the **Add Repo** button.  
   ![Databricks Add Repo](./images/Databricks%20Add%20Repo.png)

6. Once the *Add Repo* dialog box appears, paste the repository link into **Git repository URL**. The *Git Provider* and *Repository name* will automatically be populated. And then click on the **Submit** button.  
   ![Databricks Add Repo Submit](./images/Databricks%20Add%20Repo%20Submit.png)

The Azure DevOps repo will appear in the *Repos* blade once it is successfully added.  
   ![Databricks Repo Successfully Added](./images/Databricks%20Repo%20Successfully%20Added.png)

## Cloning the ELT-Framework folder in Databricks

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the *Azure Databricks page is loaded, click on **Repos** Label. Once the repo blade is open, click on **MDP-Framework > DataBricks**.  
   ![Databricks - Repos ELT Framework folder](./images/Databricks%20-%20Repos%20ELT%20Framework%20folder.gif)

6. Once you have reached to the **Databricks** folder, on the **ELT-Framework** folder, click on down arrow and then expand the **Export** label and then click on the **DBC Archive** button. This will download the *ELT-Folder* into a DBC Archive file.  
   ![Databricks - Export DBC Archive](./images/Databricks%20-%20Export%20DBC%20Archive.png)

7. Once you have downloaded, the *ELT-Folder*, click on the **Workspace** label. Once the *Workspace* blade is open, click on the down arrow on to expand the **Workspace** dropdown and then click on the **Import** button. This will open the *Import Notebooks* dialog. Click on the **browse** link and import the **ELT-Framework DBC Archive** file and then click on the **Import** button.  
    ![Databricks - Import](./images/Databricks%20-%20Import.gif)

