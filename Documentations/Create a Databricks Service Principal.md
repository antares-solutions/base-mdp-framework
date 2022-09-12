# Introduction

This is a enterprise application so that Databricks to create secret scopes and mounting the data on top of the data lake storage. 

## Creating a Service Principal

1. Log into [Azure Portal](https://portal.azure.com/)
2. Go to Azure Active Directory.
3. From the left side menu, click on **Enterprise application**.  
   ![AAD (Enterprise Applications)](./images/AAD%20(Enterprise%20Applications).png)

4. Once the *Enterprise application* page is loaded, click on **New application** button.  
   ![ADD - Enterprise Applications (Add application)](./images/Enterprise%20Applications%20(Add%20application).png)

5. Once the *Browse Azure AD Gallery* is loaded, click on the **Create your own application** button.  
   ![ADD - Enterprise Applications (Create your own application)](./images/ADD%20-%20Enterprise%20Applications%20(Create%20your%20own%20application).png)

6. Once the **Create your own application** blade is loaded, enter the name of the app **DataBricks** and then select the **Integrate any other application you don't find in the gallery (Non-gallery)**.  
   ![ADD - Enterprise Applications (Integrate any other application you don't find in the gallery (Non-gallery))](./images/ADD%20-%20Enterprise%20Applications%20(Integrate%20any%20other%20application%20you%20don't%20find%20in%20the%20gallery%20(Non-gallery)).png)
