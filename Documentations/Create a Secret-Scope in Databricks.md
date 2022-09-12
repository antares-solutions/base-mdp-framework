# Introduction

Once the resources have been deployed; as part of the post deployment; a secret scope is required to be added within databricks.  

## Creating a Secret-Scope in Databricks

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL**.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once you have copied the URL, append the URL with `#secrets/createScope`. For the full of the url see example below.  
   > `https://<databricks-instance>#secrets/createScope`

6. Launch the above the URL in your browser. And sign in into your databricks instance. Once the page is loaded, the following below and then click the **Save** button.  
   ![Azure - Databricks Create Secret Scope](./images/Azure%20-%20Databricks%20Create%20Secret%20Scope.png)  

   In order to retrieve the Azure Key Vault *DNS Name* and *Subscription*, Go to back to your resource group and then access your Azure Key Vault resource.  
   ![Azure - Resource Group Keyvault](./images/Azure%20-%20Resource%20Group%20Keyvault.png)  

   Once your *Azure Key Vault* Overview page is loaded, click on **Properties** from the left side menu.  
   ![Azure - Key vault properties](./images/Azure%20-%20Key%20vault%20properties.png)

## Installing Databricks CLI

To verify that the secret is being created, you will need to install [python](https://www.python.org/) and install the Databricks CLI via `pip`.

1. Download [python](https://www.python.org/) if not installed.
2. Once `python` is installed, open a command line:  
   For Windows run:  

   ```cmd
      py -m pip install databricks-cli
   ```

   For MacOS and Linux run:

   ``` cmd
       To do later
   ```

3. Once the Databricks cli is installed, go to your *Azure Databricks* instance and copy the **URL**.  
   ![Azure Databricks Copy URL](./images/Azure%20Databricks%20-%20Copy%20URL.png)

4. Go to your *Azure Key vault*, once the *Overview* page is loaded, click on the **Secrets** option on left side menu. Once the *Secrets* page is loaded, click on the **Databricks-PAT** option.  
   ![Azure - Key Vaults Secret](./images/Azure%20-%20Key%20Vaults%20Secret.png)

5. Once the *Databricks-PAT* page is loaded, click on the **CURRENT VERSION** line.  
   ![Azure - Key Vaults Secret Databricks PAT](./images/Azure%20-%20Key%20Vaults%20Secret%20Databricks%20PAT.png)

6. Once the *Secret Version* page is loaded, copy the secret value.  
   ![Azure - Key Vaults Secret Version](./images/Azure%20-%20Key%20Vaults%20Secret%20Version.png)

7. Once the *Azure Databricks URL* is copied, open a another command line terminal and run the following command.  

   ```cmd
      databricks configure --token
   ```

8. The command will prompt you to enter the URL. Enter the copied *Azure Databricks URL* and past it in the terminal. When the *Token* prompt appears and the copied *Databricks PAT* into the terminal and then press the `Enter` key.  
   ![Windows Terminal - Enter Azure Databricks URL and PAT](./images/Windows%20Terminal%20-%20Enter%20Azure%20Databricks%20URL%20and%20PAT.png)

9. This will generate a `.databrickscfg` file in your `%USERPROFILE%\.databrickscfg` directory on Windows or `~/.databrickscfg` in MacOS and Linux, with the following content.  
   ![Windows databrickscfg file](./images/Windows%20databrickscfg%20file.png)  

10. After generating the `.databrickscfg` file, open another **terminal in administrator mode** and run the following command.  

    ```cmd
      setx DATABRICKS_CONFIG_FILE "%USERPROFILE%\.databrickscfg" /M
    ```

11. After running the above command, you should see the following output.  
    ![Windows Terminal - Setting Environment Variable](./images/Windows%20Terminal%20-%20Setting%20Environment%20Variable.png)

## Verifying that the secret is created

Once the Databricks CLI is installed, you will be able to check whether the secret scope is created. Run the the command `databricks secrets list-scopes` to list all the secret scopes created in Databricks.  

![Windows Terminal - Listing secret scopes](./images/Windows%20Terminal%20-%20Listing%20secret%20scopes.png)