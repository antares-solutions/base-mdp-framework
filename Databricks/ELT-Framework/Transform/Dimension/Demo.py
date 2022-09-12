# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"trusted.dbo_extractloadmanifest")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
        "SystemCode Demo_BK",
        "SystemCode",
        "SourceID",
        "Left(SourceID, 1) ID"
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
