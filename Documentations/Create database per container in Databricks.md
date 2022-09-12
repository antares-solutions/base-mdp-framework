# Introduction

Once you have linked the repo to your Databricks instance and cloned the ELT-Framework folder to the root workspace. The next step is to create databases in Databricks per container. There will be three databases created which are called:  

* Raw
* Trusted
* Curated

This is a reflection of the containers that have been created in the Azure Storage account.  
  ![Azure - Storage account containers](./images/Azure%20-%20Storage%20account%20containers.png)

## Create database per container in Databricks

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the databricks home page is loaded, open the left side menu bar and then click on **Compute** option. Once the *Compute* page is open, ensure the **All** option is select and start your default cluster.  
   ![Azure - Databricks Compute start default-cluster](./images/Azure%20-%20Databricks%20Compute%20start%20default-cluster.png)

6. Once the cluster is running. On the left side menu, click **Workspace > ELT-Framework > Common** option. Once the *Common* blade appears, click on **common-mount** notebook.  
   ![Azure - Databricks Workspace open common-mount notebook](./images/Azure%20-%20Databricks%20Workspace%20open%20common-mount%20notebook.gif)

7. Once the **common-mount** notebook is open, select the **default-cluster** from the drop down menu and then click on the **Run all cells in the notebook** button.  
   ![Azure Databricks - attach cluster and run](./images/Azure%20Databricks%20-%20attach%20cluster%20and%20run.png)

8. Once the *common-mount* notebook has ran successfully. From the left side menu, click the **Data** label. And you should see **raw**, **curated** & **trusted** databases.  
   ![Azure Databricks - Data label](./images/Azure%20Databricks%20-%20Data%20label.png)