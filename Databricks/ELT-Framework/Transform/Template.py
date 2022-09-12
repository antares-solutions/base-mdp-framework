# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def Transform():
    # ------------- TABLES ----------------- #
    df = GetTable(f"TRUSTED_TABLE_NAME")
    # ------------- JOINS ------------------ #

    # ------------- TRANSFORMS ------------- #
    _.Transforms = [
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
