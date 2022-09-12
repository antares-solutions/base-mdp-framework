# Introduction

In order to for Azure Data Factory to execute the curated pipeline, In ADF, you need to enable the `Transform` variable in the `Main` pipeline and then  entries are required to be added to the `ControlDB` in table `dbo.TransformManifest`. The SQL code below will be used for adding entries into the `dbo.TransformManifest`.  

   ```sql
   Begin

    DECLARE @TransformID INT = 1001
    DECLARE @EntityType VARCHAR(50) = 'Dimension'
    DECLARE @EntityName VARCHAR(50) = 'd_purchaseorders'
    DECLARE @ProcessorType VARCHAR(30) = 'databricks-notebook'
    DECLARE @TargetKeyVaultSecret VARCHAR(50) = 'Source-WideWorldImporters'
    DECLARE @Command VARCHAR(50) = 'Transform/Dimension/PurchaseOrders'
    DECLARE @Dependencies VARCHAR(30) = ''
    DECLARE @ParallelGroup INT = 1
    DECLARE @Enabled BIT = 1
    DECLARE @CreatedDTS DATETIME = GETDATE()

    Insert into dbo.TransformManifest
    Select @TransformID
    ,@EntityType
    ,@EntityName
    ,@ProcessorType
    ,@TargetKeyVaultSecret
    ,@Command
    ,@Dependencies
    ,@ParallelGroup
    ,@Enabled
    ,@CreatedDTS

    End
   ```

The definitions for the variables used for the insertion are:  

|Variable Name        |Description                                                        |
|---------------------|-------------------------------------------------------------------|
|@TransformID         |Incremental ID for insertion into `dbo.TransformManifest`.         |
|@EntityType          |Whether the entity type is a dimension or a fact.                  |
|@EntityName          |Entity Name is the name of the curated layer.                      |
|@ProcessorType       |Default code is `databricks-notebook`.                             |
|@TargetKeyVaultSecret|Key Vault Secret used to access data from source.                  |
|@Dependencies        |providing any inter table dependencies.                            |
|@ParallelGroup       |Used to run the notebooks in parallel and helps in reduced runtime.|
|@Enabled             |Used to enable the curated notebook to run.                        |
|@CreatedDTS          |Insert current datetime during insertion.                          |

## Enabling Curated Pipeline in ADF

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to your resource group and click on the ADF resource.  
   ![Azure - Resource Group open ADF resource](./images/Azure%20-%20Resource%20Group%20open%20ADF%20resource.png)

3. Once *Azure Data factory* page is loaded, click on **Open Azure Data Factory Studio** button.  
   ![Azure Data Factory Open Azure Data Factory Studio](./images/Azure%20-%20Azure%20Data%20Factory%20Open.png)

4. Once the *Azure data factory* home page is open click on the author Label on the left side menu.  
   ![Azure Data Factory Homepage - Author](./images/Azure%20Data%20Factory%20Homepage%20-%20Author.png)

5. Once the **Factory Resources** page is open, expand the **Pipelines > ELT-Framework** tree. One the *ELT-Framework* folder is open, click on the **Main** pipeline. Once the *Main* page is loaded, click on the **Variables** tab. Once the variable tab is open, change **Transform** value from `false` to `true`. And then click on the **Save** button and then click on the **Publish** button.  
   ![Azure Data Factory - Change Transform Value](./images/Azure%20Data%20Factory%20-%20Change%20Transform%20Value.png)

## Adding Entries into control DB

1. Open SQL Server Management Studio or Azure Data Studio and log into the Control DB server.  
   ![SMSS - Login](./images/SMSS%20-%20Login.png)

2. Once you have logged into the SQL Server, ensure that `ControlDB` database is selected and then click on the **New Query** button.  
   ![SSMS - New Query](./images/SSMS%20-%20New%20Query.png)

3. For adding the entry for the `d_purchaseorders`, please execute the SQL code below.  

   ```sql
   Begin

    DECLARE @TransformID INT = 1001
    DECLARE @EntityType VARCHAR(50) = 'Dimension'
    DECLARE @EntityName VARCHAR(50) = 'd_purchaseorders'
    DECLARE @ProcessorType VARCHAR(30) = 'databricks-notebook'
    DECLARE @TargetKeyVaultSecret VARCHAR(50) = 'Source-WideWorldImporters'
    DECLARE @Command VARCHAR(50) = 'Transform/Dimension/PurchaseOrders'
    DECLARE @Dependencies VARCHAR(30) = ''
    DECLARE @ParallelGroup INT = 1
    DECLARE @Enabled BIT = 1
    DECLARE @CreatedDTS DATETIME = GETDATE()

    Insert into dbo.TransformManifest
    Select @TransformID
    ,@EntityType
    ,@EntityName
    ,@ProcessorType
    ,@TargetKeyVaultSecret
    ,@Command
    ,@Dependencies
    ,@ParallelGroup
    ,@Enabled
    ,@CreatedDTS

    End
   ```

4. Repeat step 3 for adding the `d_purchaseorderslines` & `d_suppliers` entries (please increment the `@TransformID` variable as you execute the SQL statement).
5. For adding the entry for the `f_purchaseorders`, please execute the SQL code below.  

   ```sql
    -- Insertion to Transform Manifest

    Begin

    DECLARE @TransformID INT = 1004
    DECLARE @EntityType VARCHAR(50) = 'Fact'
    DECLARE @EntityName VARCHAR(50) = 'f_purchaseorders'
    DECLARE @ProcessorType VARCHAR(30) = 'databricks-notebook'
    DECLARE @TargetKeyVaultSecret VARCHAR(50) = 'Source-WideWorldImporters'
    DECLARE @Command VARCHAR(50) = 'Transform/Fact/PurchaseOrders'
    DECLARE @Dependencies VARCHAR(30) = ''
    DECLARE @ParallelGroup INT = 2
    DECLARE @Enabled BIT = 1
    DECLARE @CreatedDTS DATETIME = GETDATE()

    Insert into dbo.TransformManifest
    Select @TransformID
    ,@EntityType
    ,@EntityName
    ,@ProcessorType
    ,@TargetKeyVaultSecret
    ,@Command
    ,@Dependencies
    ,@ParallelGroup
    ,@Enabled
    ,@CreatedDTS

    End

    SELECT * 
    FROM dbo.TransformManifest   
   ```

6. Once you have added all the entries that is required for the curated pipeline. The entries should appear as per the below screenshot.  
   ![SSMS - Rows added into dbo.TransformManifest](./images/SSMS%20-%20Rows%20added%20into%20dbo.TransformManifest.png)


## Executing the pipeline

Once the curated pipeline is enabled and entries are added into dbo.TransformManifest. Follow the documentation for [Execute the main pipeline](./Execute%20the%20main%20pipeline.md) for SystemCode `WWI-Purchasing`.