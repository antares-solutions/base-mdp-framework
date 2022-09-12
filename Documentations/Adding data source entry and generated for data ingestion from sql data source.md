# Introduction

After setting up databricks and Azure Data Factory, this step involves adding an entry in Azure key vault and manifest data into the control DB for ingesting data through the MDP framework.  

## Adding SQL Data source into Azure Key vault & adding an entry in the control DB

1. Firstly, you will need to added your data source and, database server, database, user name and password into the connection string below.  

   ```text
     Server=tcp:{servername}.database.windows.net,1433;Database={databasename};User ID={username}@{servername};Password={password};Trusted_Connection=False;Encrypt=True;Connection Timeout=30
   ```  

   > Find and replace **{servername}** with Database Server name, **{databasename}** with Database server name, **{username}** with Database username & **{password}** with Database Password.

2. Log into the [Azure Portal](https://portal.azure.com/)
3. Go to your resource group and then click on your **Azure key vault** resource.  
   ![Azure - Resource Group - Azure key vault](./images/Azure%20-%20Resource%20Group%20-%20Azure%20key%20vault.png)

4. Once the *Azure key vault* overview page is loaded, click on the **Secrets** label on the left side menu.  
   ![Azure Key vault - Secrets](./images/Azure%20Key%20vault%20-%20Secrets.png)

5. Once the *Secrets* page is loaded, click on the **+ Generate/Import** button.  
   ![Azure Key vault - Secrets - Generate-Import](./images/Azure%20Key%20vault%20-%20Secrets%20-%20Generate-Import.png)

6. Once the *Create a secret* page is loaded, enter **Name** as **Source-WideWorldImporters** and enter **Value** with the connection string from *Step 1*. Lastly, click on the **Create** button to add the entry.  
   ![Azure Key vault - Create a secret](./images/Azure%20Key%20vault%20-%20Create%20a%20secret.png)

You will be redirected to the *Secrets* page, with your secret entry for your data source.  
   ![Azure Key vault - Secrets - Secret Added](./images/Azure%20Key%20vault%20-%20Secrets%20-%20Secret%20Added.png)

### Adding an entry into the control DB for data ingestion

Once the entry has been added to `dbo.ExtractLoadManifest` table with the `dbo.AddIngestion`, then we can use the `update-source-metadata` pipelines to generate and store the table metadata into the `dbo.ExtractLoadManifest` record.

1. Open SQL Server Management Studio or Azure Data Studio and log into the Control DB server.  
   ![SMSS - Login](./images/SMSS%20-%20Login.png)

2. Once you have logged into the SQL Server, ensure that `ControlDB` database is selected and then click on the **New Query** button.  
   ![SSMS - New Query](./images/SSMS%20-%20New%20Query.png)

3. Copy and past below for executing the stored procedure for adding an entry in `dbo.ExtractLoadManifest`.  

   ```sql
        DECLARE @return_value int

        EXEC    @return_value = [dbo].[AddIngestion]
                @SystemCode = N'WWI-Sales',
                @Schema = N'Sales',
                @Table = N'Invoices',
                @Query = N'Sales.Invoices',
                @WatermarkColumn = 'LastEditedWhen',
                @SourceHandler = N'sql-load',
                @RawFileExtension = NULL,
                @KeyVaultSecret = N'Source-WideWorldImporters',
                @ExtendedProperties = NULL

        SELECT  'Return Value' = @return_value

        GO
   ```

   Please see below definition of the variables used in `dbo.AddIngestion` stored procedure.  
   |Variable Name        |Description                                                                                                     |
   |---------------------|----------------------------------------------------------------------------------------------------------------|
   |`@SystemCode`        |The `@SystemCode` ties in the tables that will be ingested from your data source.                               |
   |`@Schema`            |Contains the name of the table schema from the data source.                                                     |
   |`@Table`             |Contains the table name from the data source                                                                    |
   |`@Query`             |Contains the query that will be used for the extraction.                                                        |
   |`@WatermarkColumn`   |This defines the latest record that was loaded & it's appropriate column name that will be used in the pipeline.|
   |`@SourceHandler`     |Pipeline that will be executed in ADF.                                                                          |
   |`@RawFileExtension`  |The format file that will be when the files out outputted into the Azure Storage Blob.                          |
   |`@KeyVaultSecret`    |Retrieve secret value from Key vault that will be used in the ADF pipeline execution.                           |
   |`@ExtendedProperties`|This properties to change the target table in the Data warehouse.                                               |

4. Repeat steps 2 to 3 for adding additional tables for ingestion.

Once you have executed the stored procedure, this will add an entry in the extract load manifest table.  
  ![SSMS - Query ExtractLoadManifest table](./images/SSMS%20-%20Query%20ExtractLoadManifest%20table.png)

### Executing the `update-source-metadata` Pipeline for generating the Source Metadata

Once an entry is added to the `dbo.ExtractLoadManifest` table. It is now time to generate the metadata which will be used to mapped to the output file.

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to your resource group and click on the ADF resource.  
   ![Azure - Resource Group open ADF resource](./images/Azure%20-%20Resource%20Group%20open%20ADF%20resource.png)

3. Once *Azure Data factory* page is loaded, click on **Open Azure Data Factory Studio** button.  
   ![Azure Data Factory Open Azure Data Factory Studio](./images/Azure%20-%20Azure%20Data%20Factory%20Open.png)

4. Once the *Azure data factory* home page is open click on the author Label on the left side menu.  
   ![Azure Data Factory Homepage - Author](./images/Azure%20Data%20Factory%20Homepage%20-%20Author.png)

5. Once the *Author* page is loaded, expand the *Pipelines* tree, *ELT-Framework* folder, *Metadata* sub folder then the *Setup* sub folder. Lastly, click on the **update-source-metadata** pipeline. Once the *update-source-metadata* is opened in the editor, click on the **Add Trigger** button and then click on **Trigger Now**.  
   ![Azure Data Factory - expand pipeline folder to update](./images/Azure%20Data%20Factory%20-%20expand%20pipeline%20folder%20to%20update.png)

6. Once the *Pipeline* blade appears, enter the system code for the entries you have created in `dbo.ExtractLoadManifest` table and then click on the **OK button**.  
   ![Azure Data Factory - Pipeline run blade](./images/Azure%20Data%20Factory%20-%20Pipeline%20run%20blade.png)

7. Once the pipelines has ran successfully, in the **ControlDB** you will see that the `dbo.ExtractLoadManifest.SourceQuery` and `dbo.ExtractLoadManifest.SourceMetaData` columns has been updated.  
   ![Azure Data Factory - Successful Run](./images/Azure%20Data%20Factory%20-%20Successful%20Run.png)

   ![SSMS - SourceQuery & SourceMetaData columns updated](./images/SSMS%20-%20SourceQuery%20%26%20SourceMetaData%20columns%20updated.png)
