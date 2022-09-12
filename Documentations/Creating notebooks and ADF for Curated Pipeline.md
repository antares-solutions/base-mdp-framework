# Introduction

Setting up notebooks and ADF is the last step for the curated pipeline. The curated pipeline is responsible for generating the dimensions and fact tables which will be used by the end user when building reports in Power BI or any other reporting tool.

In this example we will creating notebooks for transforming data from the Wide World Importers Database from the `Purchasing` schema.

## Cloning Dimension notebooks for the Curated Layer

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the *Databricks* home page is loaded, click on **Repos** label. Once the *Repos* blade is open, click on **MDP-Framework > Databricks > ELT-Framework**. Once you have reached the *ELT-Framework* folder expand the menu by clicking the down arrow and the `Template` file and then click on the **Clone** label.  
    ![Databricks - Clone Template file](./images/Databricks%20-%20Clone%20Template%20file.gif)

6. Once the *Cloning 'Template'* dialog box appears, rename your file to `PurchaseOrders` and then click on the **Transform > Dimension** folder and then click on the **Clone** button.  
   ![Databricks - Clone Template file completed](./images/Databricks%20-%20Clone%20Template%20file%20completed.gif)

7. Once the cloning of the `Template` file is completed, go to **Transform > Dimension** and open the cloned file that was renamed.  
   ![Databricks - Opening cloned file](./images/Databricks%20-%20Opening%20cloned%20file.gif)

8. Repeat steps 5 to 6 for creating a notebook for `PurchaseOrderLines`.

### Using trusted table for transforming data into a dimension in the curated layer

After executing the main pipe from [Execute the main pipeline](./Documentations/Execute%20the%20main%20pipeline.md) documentation. The `raw` and `trusted` databases will be mounted in databricks. For the curated layer, we only need to use tables from the `trusted` schema.  

![Databricks - trusted schema purchasing table](./images/Databricks%20-%20trusted%20schema%20purchasing%20table.png)

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the *Databricks* home page is loaded, click on **Repos** label. Once the *Repos* blade is open, click on **MDP-Framework > Databricks > ELT-Framework > Transform > Dimension**, once you have reached the *Dimension* folder, click on the **Purchase Order** notebook.  
   ![Databricks - Purchase Order Notebook](./images/Databricks%20-%20Purchase%20Order%20Notebook.gif)

6. Once the *Purchase Order* notebook is open, on line 3, change `TRUSTED_TABLE_NAME` to `purchasing_purchaseorders` & on line 8 change `BK_REFERENCE` to `PurchaseOrderID PurchaseOrders_BK`. Once you have made all the updates, click on the **Run all** to verify that the table is created in the **curated** database.  
   ![Databricks - Purchase Order Notebook updates](./images/Databricks%20-%20Purchase%20Order%20Notebook%20updates.png)

7. Once the notebook has successfully ran, you will see a record count and the creation of the table in the `curated` database.  
   ![Databricks - Run purchase order notebook](./images/Databricks%20-%20Run%20purchase%20order%20notebook.png)

8. Click on **Data > `hive_metastore` > `curated` > `d_purchaseorders`. This will show you sample view of the table an data.  
   ![Databricks - Data to d_purchaseorders](./images/Databricks%20-%20Data%20to%20d_purchaseorders.png)

9. Repeat Steps 5 to 8 for creating a curated notebook and table for `purchasing_purchaseorderlines` & `purchasing_suppliers` table from the `trusted` table.

## Creating Fact notebooks for the Curated Layer

Creating the Fact notebooks for the Curated Layers follows the similar process as creating notebook for Dimension tables.

1. Follow steps 1 to 5 from [Cloning Dimension notebooks for the Curated Layer](./Creating%20notebooks%20and%20ADF%20for%20Curated%20Pipeline.md#cloning-dimension-notebooks-for-the-curated-layer) documentation.

2. Once the *Cloning 'Template'* dialog box appears, rename your file to `PurchaseOrders` and then click on the **Transform > Fact** folder and then click on the **Clone** button.  
   ![Databricks - Clone template file to Fact folder](./images/Databricks%20-%20Clone%20template%20file%20to%20Fact%20folder.png)

3. Replace line 3 with the following code below.  

   ```python
    PurchaseOrdersdf = spark.table(f"{DEFAULT_TARGET}.d_purchaseorders")
    PurchaseOrderLinesdf = spark.table(f"{DEFAULT_TARGET}.d_purchaseorderslines")
    Suppliers = spark.table(f"{DEFAULT_TARGET}.d_suppliers")      
   ```

4. Copy the code below and paste into line 5.  

   ```python
    df = PurchaseOrdersdf.join(PurchaseOrderLinesdf, (PurchaseOrdersdf.PurchaseOrders_BK == PurchaseOrderLinesdf.PurchaseOrdersLines_BK), "inner")
    df = df.join(Suppliers, df.SupplierID == Suppliers.Suppliers_BK)      
   ```

5. Copy the code below and paste into lines 7 to 10.  

   ```python
    _.Transforms = [
        "PurchaseOrders_BK",
        "SupplierName",
        "PurchaseOrderLineID",
        "Description",
        "OrderedOuters",
        "ReceivedOuters",
        "ExpectedUnitPricePerOuter",
        "IsOrderLineFinalized"
    ]   
   ```

   Once you have copied and pasted all the code from steps 3 to 5. your notebook should appear in the screenshot below.  
   ![Databricks - Fact PurchaseOrders](./images/Databricks%20-%20Fact%20PurchaseOrders.png)

6. Click on the **Run All** button to run the notebook. Once the notebook has successfully finished running, you will see an output of statistics of records count and curated transform output of `f_PurchaseOrders`.  
   ![Databricks - Fact PurchaseOrders notebook ran](./images/Databricks%20-%20Fact%20PurchaseOrders%20notebook%20ran.png)

## Cloning created Dimension and Fact Notebooks to `ELT-Framework` folder

Once you have created and tested your dimension and fact notebooks. You will need to the `ELT-Framework` folder in **Workspaces**.

1. Log into [Azure Portal](https://portal.azure.com/).
2. Find and go to your **Resource Group** where you have deployed the azure resources required for the MDP framework.  
   ![Azure - Homepage](./images/Azure%20-%20Homepage.png)

3. Once the *Resource Group* page is loaded, click on your **Azure Databricks Service** resource.  
   ![Azure - MDP Framework Resource Group](./images/Azure%20-%20MDP%20Framework%20Resource%20Group.png)

4. Once the *Azure Databricks Service* resource is loaded, click on the **Copy** button to copy the **Azure Databricks Service URL** and paste it into your browser.  
   ![Azure - Databricks Service URL](./images/Azure%20-%20Databricks%20Service%20URL.png)

5. Once the *Databricks* home page is loaded, click on **Repos** label. Once the *Repos* blade is open, click on **MDP-Framework > Databricks > ELT-Framework > Transform > Dimension**. Once you have reached to the Dimension folder, click on the down arrow to open the menu and then expand **Export** menu and then click on the **DBC Archive** and which will download to your default download location on your computer.  
   ![Databricks - Export Dimensions](./images/Databricks%20-%20Export%20Dimensions.png)

6. Repeat Step 5 for exporting the **Fact** folder into a **DBC Archive**.  
   ![Databricks - Export Facts](./images/Databricks%20-%20Export%20Facts.png)

7. Once you have exported both **Dimension** & **Fact** folder into DBC Archive. Click on the **Workspace** label, and then go to **EFT-Framework > Transform** folder. Once you have reached to the *Transform* folder, click on the down arrow to expand the menu and then click on the **Import** button.  
   ![Databricks - Importing DBC](./images/Databricks%20-%20Importing%20DBC.png)

8. Once the *Import Notebooks* appears, click on the **browse** link and then click on upload `Dimension.dbc` file.  
    ![Databricks - Import Dimension.dbc file](./images/Databricks%20-%20Import%20Dimension.dbc%20file.png)

9. Repeat step 8 for importing the `Fact.dbc` file.  

10. Once you have imported both `*.dbc` files, they should appear in the **Transform** folder.  
    ![Databricks - Workspace Transform folder](./images/Databricks%20-%20Workspace%20Transform%20folder.png)