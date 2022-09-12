# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.sales_orderlines")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "OrderLineID",
        "OrderID SalesOrderLines_BK",
        "StockItemID",
        "Description",
        "PackageTypeID",
        "Quantity",
        "UnitPrice",
        "TaxRate",
        "PickedQuantity",
        "PickingCompletedWhen",
        "LastEditedBy",
        "LastEditedWhen"
    ]
    
    df = df.selectExpr(
        _.Transforms
    )

    # ------------- CLAUSES ---------------- #

    # ------------- SAVE ------------------- #
    #display(df)
    Save(df)

pass

Transform()    
