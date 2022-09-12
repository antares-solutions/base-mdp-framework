# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.sales_invoicelines")
    # ------------- JOINS ------------------ #
    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "InvoiceLineID",
        "InvoiceID SalesInvoiceLines_BK",
        "StockItemID",
        "Description",
        "PackageTypeID",
        "Quantity",
        "UnitPrice",
        "TaxRate",
        "TaxAmount",
        "LineProfit",
        "ExtendedPrice",
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
    
