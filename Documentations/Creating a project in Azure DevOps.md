# Introduction

Currently, the MDP framework requires Azure DevOps for deployment of resource and code. Once you have downloaded the MDP framework solution, you will first need to create a service connector to your azure resource group and then deployment of rescuer and code will follow.

**Note:** If you have created a *Free* Azure DevOps account, you will need to raise a request to Microsoft for a Free Tier License for Parallel Jobs. See link [Azure DevOps Parallelism Request](https://forms.office.com/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbR63mUWPlq7NEsFZhkyH8jChUMlM3QzdDMFZOMkVBWU5BWFM3SDI2QlRBSC4u).

## Creating a Project

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Click on the **Create Project** button.  
   ![Azure DevOps (Create Project)](./images/Azure%20DevOps%20(Create%20Project).png)

3. Once the *Create new project* blade appears, enter the project name and then click on the **Project Name** and then click on the **Create** Button.  
   ![Azure DevOps (Create new project blade)](./images/Azure%20DevOps%20(Create%20new%20project%20blade).png)

4. Once the project is created and the project is loaded, click on the **Project Settings** button on the left side menu.  
   ![Azure DevOps (Project Settings)](./images/Azure%20DevOps%20(Project%20Settings).png)

5. Once the *Project Setting* page is loaded; under the *Pipeline* section, click on the **Service connections** option.  
   ![Azure DevOps (Pipeline - Service Connections)](./images/Azure%20DevOps%20(Pipeline%20-%20Service%20Connections).png)

6. Once the *Service Connections* page is loaded click on the **Create service connection** button.  
   ![Azure DevOps (Create service connection)](./images/Azure%20DevOps%20(Create%20service%20connection).png)

7. Once the *New service connection* blade appears, select the **Azure Resource Manager** and then scroll down to the bottom of the blade, click on the **Next** button.  
   ![Azure DevOps (Select Azure Resource Manager)](./images/Azure%20DevOps%20(Select%20Azure%20Resource%20Manager).gif)

8. Once the *New Azure service connection* is loaded onto the blade, click on **Service principal (manual)**.  
   ![Azure DevOps (New Azure service connection - Service principal (manual))](./images/Azure%20DevOps%20(New%20Azure%20service%20connection%20-%20Service%20principal%20(manual)).png)

9. Once the **New Azure service connection** blade appears, the following:
   * Subscription Id
   * Subscription Name
   * Service Principal Id (Application (client) ID from App Registration)
   * Service principal key (App Secret from App Registration)
   * Tenant ID

10. Once the above details are entered, click on the verified button to verify the information entered and the **Service connection name** and then click on the **Verify and save** button.  
    ![Azure DevOps (Enter New Azure service connection)](./images/Azure%20DevOps%20(Enter%20New%20Azure%20service%20connection).png)

11. After clicking the *Verify and save* button, the Service Connection will be created.  
    ![Azure DevOps (Service connection created)](./images/Azure%20DevOps%20(Service%20connection%20created).png)

## Downloading the code from Github

> To do, will come back later once Azure DevOps repo is setup.

## Uploading into Azure DevOps

Once you have downloaded the MDP solution, you will need to do an initial commit into Azure DevOps repository.

1. Open a terminal to where you have downloaded the MDP framework.
2. Enter `git init` to initialize an empty git repository.
3. Go to Azure Devops -> Repos and then copy the **push an existing repository from command line**.  
   ![Azure DevOps - Repos (Copy Push an existing repository from command line)](./images/Azure%20DevOps%20-%20Repos%20(Copy%20Push%20an%20existing%20repository%20from%20command%20line).png)

4. Paste it into the terminal to add origin and the push to.  
   ![Azure DevOps - Repos (Paste Push an existing repository from command line)](./images/Azure%20DevOps%20-%20Repos%20(Paste%20Push%20an%20existing%20repository%20from%20command%20line).png)

5. Run command to add files to local repository with `git add .`
6. Perform initial commit with `git commit -m "MDP Project added"`.
7. Run `git push -u origin master` to push to the **master branch**.
