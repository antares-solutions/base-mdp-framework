# Introduction

Azure Data Factory is used for orchestration of building the data where house. Executing the main pipelines will executed pipelines that generated data and store in the Azure Storage Container (data lake). The types of data that will exported to the following containers are:

* Raw - Performs source extraction for the configured source handler. It directs to the necessary pipelines under SourceHandler to extract data onto raw zone on the data lake and creates a table for that path on Databricks.  
* Trusted - Orchestrates the call of forming the trusted zone on Databricks. It copies last known raw records and creates/updates the trusted database.
* Curated - Is the final stage which performs the orchestration of the transformations needed to update the facts or dimensions. Depending on the configuration, this will either call Databricks notebooks or Synapse/Database stored procedures in linear fashion.  

> **Please note**: Curated pipeline requires additional jupyter notebooks where ETL is performed when generating data for Dimension and Fact tables to fit your organizations needs.

## Execute the main pipeline

1. Log into the [Azure Portal](https://portal.azure.com/)
2. Go to your resource group and click on the ADF resource.  
   ![Azure - Resource Group open ADF resource](./images/Azure%20-%20Resource%20Group%20open%20ADF%20resource.png)

3. Once *Azure Data factory* page is loaded, click on **Open Azure Data Factory Studio** button.  
   ![Azure Data Factory Open Azure Data Factory Studio](./images/Azure%20-%20Azure%20Data%20Factory%20Open.png)

4. Once the *Azure data factory* home page is open click on the author Label on the left side menu.  
   ![Azure Data Factory Homepage - Author](./images/Azure%20Data%20Factory%20Homepage%20-%20Author.png)

5. Once the *Author* page is loaded, expand the *Pipelines* tree, *ELT-Framework* folder and then click on the **Main** pipeline label.  Once the *Main* pipeline is open on, click on the **Add Trigger** and then click on **Trigger now**.  
   ![Azure Data Factory Author - Main - Trigger Now](./images/Azure%20Data%20Factor%20Author%20-%20Main%20-%20Trigger%20Now.png)

6. Once the *Pipeline run* blade appears, enter the system value `WWI-Sales` and then click on the **OK** button.  
   ![Azure Data Factory - Main - Pipeline Run](./images/Azure%20Data%20Factory%20-%20Main%20-%20Pipeline%20Run.png)

7. Once the pipeline has ran successfully, parquet files will appear in the Azure storage containers.  
   ![Azure Data Factory - Main Pipeline Successful execution](./images/Azure%20Data%20Factory%20-%20Main%20Pipeline%20Successful%20execution.png)

   ![Azure Data Factory - Azure Storage Blob - Raw](./images/Azure%20Storage%20Blob%20-%20Raw.png)

   ![Azure Data Factory - Azure Storage Blob - Trusted](./images/Azure%20Data%20Factory%20-%20Azure%20Storage%20Blob%20-%20Trusted.png)