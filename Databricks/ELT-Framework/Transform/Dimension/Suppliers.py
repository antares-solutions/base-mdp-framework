# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"{DEFAULT_SOURCE}.purchasing_suppliers")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "SupplierID Suppliers_BK",
        "*"
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
