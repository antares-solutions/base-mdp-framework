# Introduction

Once the MDP Framework is in the Azure DevOps repository. A release and pipeline will be required to be setup.

## Creating Pipeline & Artifacts

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the *Summary* page is loaded, click on the **Pipelines** button on the left side menu.  
   ![Azure DevOps (Pipelines)](./images/Azure%20DevOps%20(Pipelines).png)

4. Once the *Pipelines* page is loaded, click on the **Create Pipeline** button.  
   ![Azure DevOps - Pipelines (Create Pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(Create%20Pipeline).png)

5. Once the *Where is your code?* page is loaded, click on the **Azure Repos Git** option.  
   ![Azure DevOps - Pipelines (Azure Repos Git)](./images/Azure%20DevOps%20-%20Pipelines%20(Azure%20Repos%20Git).png)

6. Once the *Select a repository* page is loaded, select your **MDP Framework Repository**.  
   ![Azure DevOps - Pipelines (Select your repository)](./images/Azure%20DevOps%20-%20Pipelines%20(Select%20your%20repository).png)

7. Once the *Configure your pipeline* page is loaded, click on **Existing Azure Pipelines YAML file** option.  
   ![Azure DevOps - Pipelines (Existing Azure Pipelines YAML file)](./images/Azure%20DevOps%20-%20Pipelines%20(Existing%20Azure%20Pipelines%20YAML%20file).png)

8. Once the *Select an existing YAML file* blade is loaded, open the **Path** dropdown menu select the `yml` file and then click on the **Continue** button.  
   ![Azure DevOps - Pipeline (Select an existing YAML file)](./images/Azure%20DevOps%20-%20Pipeline%20(Select%20an%20existing%20YAML%20file).png)

9. Once the *Review your pipeline YAML* page is loaded, click on the **Run** button.  
   ![Azure DevOps - Pipeline (Azure DevOps - Pipeline (Select an existing YAML file))](./images/Azure%20DevOps%20-%20Pipeline%20(Azure%20DevOps%20-%20Pipeline%20(Select%20an%20existing%20YAML%20file)).png)

10. This will build 4 artifacts which will be used when creating a release.  
    ![Azure DevOps - Pipeline (Success Run Pipelines)](./images/Azure%20DevOps%20-%20Pipeline%20(Success%20Run%20Pipelines).png)

## Download `IaC-CD.json` file for Azure Resource Deployment

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the summary page is loaded, expand the **Repos** menu and then click on the **Files** option.  
   ![Azure DevOps (MDP-Framework Files)](./images/Azure%20DevOps%20(MDP-Framework%20Files).png)

4. Once the git repository is loaded, expand the `.pipelines` folder and download the `IaC-CD.json` file.  
   ![Azure DevOps (IaC-CD.json file)](./images/Azure%20DevOps%20(IaC-CD.json%20file).png)

Once the `IaC-CD.json` file is downloaded, we will use this file to create a release.

## Creating group variables

The group variables are required for the MDP Framework, in order to do the deployment of Azure resources. Four variable groups are required for deploying resources into:  

* SHARED
* DEV
* UAT
* PROD

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the *Summary* page is loaded, click on the **Pipelines** button on the left side menu to expand the *Pipeline* options and then click on the **Library** option.  
   ![Azure DevOps - Pipelines (Library)](./images/Azure%20DevOps%20-%20Pipelines%20(Library).png)

4. Once the *Library* page is loaded, click on the **+ Variable group** button.
   ![Azure DevOps - Pipelines (Add Variable group)](./images/Azure%20DevOps%20-%20Pipelines%20(Add%20Variable%20group).png)

5. Once the *New variable group* page is loaded, Enter *VG-SHARED* in the **Variable group name**. And then create the following variables:
   |Variable Name                 |Input Value Description                                                                                                                                                  |
   |------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   |AAD-Group-Name                |AAD Group Name                                                                                                                                                           |
   |ADD-Group-ObjectID            |Object ID for AAD Group                                                                                                                                                  |
   |AzureDatabricks-ObjectID      |Object ID from [Service Principal for Azure Databricks](./Creating%20Service%20Principal%20For%20DataBricks.md).                                                         |
   |database-User                 |Service Account User Name for `ControlDB`                                                                                                                                |
   |location                      |Location of deployed Azure resource                                                                                                                                      |
   |resource-template             |Naming macro of Azure Resources. E.g `$RES$-base-mdp-$ENV$-01`                                                                                                           |
   |ServicePrincipal-ApplicationID|Service principal Application ID that is created for deploying Azure resources into. See [Service Principal creation documentation](./Creating%20Service%20Principal.md).|
   |ServicePrincipal-Name         |Service principal Name. See [Service Principal creation documentation](./Creating%20Service%20Principal.md).                                                             |
   |ServicePrincipal-ObjectID     |Service principal Object Id. See [Service Principal creation documentation](./Creating%20Service%20Principal.md).                                                        |
   |ServicePrincipal-Secret       |Service principal Secret. See [Service Principal creation documentation](./Creating%20Service%20Principal.md).                                                           |
   |Subscription-ID               |Azure Subscription Id.                                                                                                                                                   |
   |Tenant-ID                     |Azure Tenant Id.                                                                                                                                                         |  

   ![Azure DevOps - Pipelines (VG-Shared Variables)](./images/Azure%20DevOps%20-%20Pipelines%20(VG-Shared%20Variables).png)

6. Once the `VG-SHARED` variable group is created, click on the **Library** from the top link or from the left side menu.  
   ![Azure DevOps - Pipeline (Library 2)](./images/Azure%20DevOps%20-%20Pipeline%20(Library%202).png)

7. Once you have returned to the *Library* page, click on the **+ Variable group** button again.  
   ![Azure DevOps - Pipelines (Add VG-DEV Variable group)](./images/Azure%20DevOps%20-%20Pipelines%20(Add%20VG-DEV%20Variable%20group).png)

8. Once the *New variable group* page is loaded, Enter *VG-DEV* in the **Variable group name**. And then create the following variables:  
   |Variable Name    |Input Value                 |
   |-----------------|----------------------------|
   |database-Password|Password for ControlDB      |
   |environment      |Name of environment         |
   |resource-Group   |Name of Azure Resource Group|  
   ![Azure DevOps - Pipelines (Variables VG-DEV)](./images/Azure%20DevOps%20-%20Pipelines%20(Variables%20VG-DEV).png)

9. Repeat steps 6 to 8 for UAT and PROD.

Once you have created the Variable groups, this will be utilize when creating a release.

## Build Release Artifacts

Once the pipeline is created and the artifacts is created, a release needs to be created.

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the *Summary* page is loaded, click on the **Pipelines** button on the left side menu.  
   ![Azure DevOps (Pipelines)](./images/Azure%20DevOps%20(Pipelines).png)

4. Once the *Pipelines* menu is expanded, click on the **Release** option.  
   ![Azure DevOps - Pipelines (Releases)](./images/Azure%20DevOps%20-%20Pipelines%20(Releases).png)

5. Once the *Release* page is loaded, click on the **New pipeline** button.  
   ![Azure DevOps - Pipelines (New pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(New%20pipeline).png)

6. Once the *All pipelines* page is open and the *Select a template* blade is open, scroll down and click on the **Empty job** option and then click on the **Apply** button.  
   ![Azure DevOps - Pipelines (Empty job)](./images/Azure%20DevOps%20-%20Pipelines%20(Empty%20job).png)

7. Once the *Stage* blade is loaded, click on the **Save** button.  
   ![Azure DevOps - Pipelines (Stage - Save)](./images/Azure%20DevOps%20-%20Pipelines%20(Stage%20-%20Save).png)

8. Once the *Save* dialog appears click on the **OK** button.  
   ![Azure DevOps - Pipelines (Save Release)](./images/Azure%20DevOps%20-%20Pipelines%20(Save%20Release).png)

9. Once the *New release pipeline* is saved on the **Releases** from the left side menu. Once the New release pipeline page is loaded, click on the **New** dropdown menu and then click on **Import release pipeline**.  
   ![Azure DevOps - Pipelines (Import release pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(Import%20release%20pipeline).png)

10. Once the *Import release pipeline* dialog appears click on the **Browse** button, once the *File Dialog* opens, find and select your `IaC-CD.json` file and then click on the .  
   ![Azure DevOps - Pipelines (Import IaC-CD.json file)](./images/Azure%20DevOps%20-%20Pipelines%20(Import%20IaC-CD.json%20file).png)

11. Once the `IaC-CD.json` is imported, click on the `_build` artifact and then **delete** it.  
    ![Azure DevOps - Pipelines (Delete _build artifact)](./images/Azure%20DevOps%20-%20Pipelines%20(Delete%20_build%20artifact).png)

12. Once deleted, click on the **Add an artifact** button. Once the **Build an artifact** blade appears, open the **Source (build pipeline)** drop down menu and select *MDP-Framework*. Then change the **Source alias** to `_build`. Lastly, click on the **Add** button.  
    ![Azure DevOps - Pipelines (Add an artifact)](./images/Azure%20DevOps%20-%20Pipelines%20(Add%20an%20artifact).png)

### Configuring job and and stages for Azure resource deployment

Once the artifact is added, you will now need to configure the job and task in the **Stages** section.

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the `IaC-CD` pipeline is loaded click on the **1 job, 7 tasks** link for **DEV** in the **Stages** section.  
   ![Azure DevOps - Pipelines (DEV job and tasks)](./images/Azure%20DevOps%20-%20Pipelines%20(DEV%20job%20and%20tasks).png)

4. Once the *Development process* page is loaded, click on the **Application** section.  
   ![Azure DevOps - Pipelines (Development process)](./images/Azure%20DevOps%20-%20Pipelines%20(Development%20process).png)

5. Once the *Agent job* section is loaded, select **Azure Pipelines** from the dropdown menu.  
   ![Azure DevOps - Pipelines (Agent pool)](./images/Azure%20DevOps%20-%20Pipelines%20(Agent%20pool).png)

6. Once the *Agent Specification* dropdown menu appears, select `windows-latest`.  
   ![Azure DevOps - Pipelines (Agent Specification)](./images/Azure%20DevOps%20-%20Pipelines%20(Agent%20Specification).png)

7. Click on the **Main Variables** section.  
   ![Azure DevOps - Pipelines (Main Variables)](./images/Azure%20DevOps%20-%20Pipelines%20(Main%20Variables).png)

8. Once the *Main Variables* section is loaded, select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) from the *Azure subscription* dropdown menu.  
   ![Azure DevOps - Pipelines (Azure subscription)](./images/Azure%20DevOps%20-%20Pipelines%20(Azure%20subscription).png)

9. In the **Resource group** dropdown menu, enter `$(resource-Group)` in the dropdown menu.  
   ![Azure DevOps - Pipelines (Enter resource group variable)](./images/Azure%20DevOps%20-%20Pipelines%20(Enter%20resource%20group%20variable).png)

10. Click on **Data Services** and select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) in the **Azure Subscription** dropdown and enter `$(resource-Group)` in the **Resource Group** dropdown menu.  
   ![Azure DevOps - Pipelines (Fill empty mandatory fields in data services)](./images/Azure%20DevOps%20-%20Pipelines%20(Fill%20empty%20mandatory%20fields%20in%20data%20services).png)

11. Click on **Application** and select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) in the **Azure Subscription** dropdown and enter `$(resource-Group)` in the **Resource Group** dropdown menu.  
   ![Azure DevOps - Pipelines (Fill empty mandatory fields in application)](./images/Azure%20DevOps%20-%20Pipelines%20(Fill%20empty%20mandatory%20fields%20in%20application).png)

12. Click on **Databricks Setup** and and select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) in the **Azure Subscription** dropdown.  
   ![Azure DevOps - Pipelines (Fill empty mandatory fields in databricks setup)](./images/Azure%20DevOps%20-%20Pipelines%20(Fill%20empty%20mandatory%20fields%20in%20databricks%20setup).png)

13. Click on **Synapse Setup** and and select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) in the **Azure Subscription** dropdown.  
   ![Azure DevOps - Pipeline (Fill empty mandatory fields in synapse setup)](./images/Azure%20DevOps%20-%20Pipelines%20(Fill%20empty%20mandatory%20fields%20in%20synapse%20setup).png)

14. Click on **Control DB** and and select the [Service Principal](./Creating%20Service%20Principal%20For%20Azure%20DevOps.md) in the **Azure Subscription** dropdown.  
   ![Azure DevOps - Pipelines (Fill empty mandatory fields in controldb)](./images/Azure%20DevOps%20-%20Pipelines%20(Fill%20empty%20mandatory%20fields%20in%20controldb).png)

15. Open the **Task** menu, and then select UAT and then PROD. Repeat steps 4 to 14 for UAT and PROD.  
   ![Azure DevOps - Pipelines (Tasks)](./images/Azure%20DevOps%20-%20Pipelines%20(Tasks).png)

16. Once you have completed entering the variables for UAT and PROD. click on the **Save** button.  
   ![Azure DevOps - Pipelines (Save Pipeline Changes)](./images/Azure%20DevOps%20-%20Pipelines%20(Save%20Pipeline%20Changes).png)

### Linking Group Variables

Once you have completed entering the pipeline configuration variables. Next is to link the group variables to the pipeline.

1. Log into [Azure DevOps](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409).
2. Go to your MDP Project.  
   ![Azure DevOps (MDP-Framework Project)](./images/Azure%20DevOps%20(MDP-Framework%20Project).png)

3. Once the `IaC-CD` pipeline is loaded click on the **1 job, 7 tasks** link for **DEV** in the **Stages** section.  
   ![Azure DevOps - Pipelines (DEV job and tasks)](./images/Azure%20DevOps%20-%20Pipelines%20(DEV%20job%20and%20tasks).png)

4. Once the *Development process* page is loaded click on the **Variables** tab.  
   ![Azure DevOps - Pipelines (Variables tab)](./images/Azure%20DevOps%20-%20Pipelines%20(Variables%20tab).png)

5. Once the *Variables* tab, click on the **Variable groups** option. And then click on **Link variable group** button.  
   ![Azure DevOps - Pipelines (Variable groups)](./images/Azure%20DevOps%20-%20Pipelines%20(Variable%20groups).png)

6. Once the *Link variable group* blade appears, select **VG-SHARED** option and click on the **Link** button.  
   ![Azure DevOps - Pipelines (Linking vg-shared to pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(Linking%20vg-shared%20to%20pipeline).png)

7. Once *VG-SHARED* is linked, click on the **Link variable group** button and link **VG-DEV**, select the **Stages** option from **Variable group scope** section and then from the dropdown menu select **DEV**. Lastly, click on the **Link** button.  
   ![Azure DevOps - Pipelines (Linking vg-dev to pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(Linking%20vg-dev%20to%20pipeline).png)

8. Repeat step 7 for UAT and DEV and then click the **Save** button and when the **Save** Dialog appears click on the **OK** button.  
   ![Azure DevOps - Pipelines (Save linked variable groups to pipeline)](./images/Azure%20DevOps%20-%20Pipelines%20(Save%20linked%20variable%20groups%20to%20pipeline).png)

## Create a release

1. Once all the variables linked to the pipeline, click on **Releases** option on the left side menu.  
   ![Azure DevOps - Pipelines (Releases)](./images/Azure%20DevOps%20-%20Pipelines%20(Releases).png

2. Once the *Release* page is loaded, click on the **Create a release** or the **Create release** button.  
   ![Azure DevOps - Releases (Create a Release)](./images/Azure%20DevOps%20-%20Releases%20(Create%20a%20Release).png)

3. Once the *Create a new release* blade is open, click on the **Create** button to deploy to start the resource into your Azure Resource source.  
   ![Azure DevOps - Pipelines (Create Release)](./images/Azure%20DevOps%20-%20Pipelines%20(Create%20Release).png)

4. This will create a Release entry for deployment.  
   ![Azure DevOps - Pipelines (Release Entry)](./images/Azure%20DevOps%20-%20Pipelines%20(Release%20Entry).png)

5. Once the deployment has successfully completed, Azure Resources into your configured resource group.  
   ![Azure DevOps - Pipelines (Successful Release)](./images/Azure%20DevOps%20-%20Pipelines%20(Successful%20Release).png)

   ![Azure - Resource Group (Azure Resource Deployed)](./images/Azure%20-%20Resource%20Group%20(Azure%20Resource%20Deployed).png)
