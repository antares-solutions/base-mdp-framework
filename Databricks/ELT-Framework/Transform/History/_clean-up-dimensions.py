# Databricks notebook source
# MAGIC %run ../../Common/common-workspace

# COMMAND ----------

from datetime import *
today = date.today().strftime("%Y%m%d")
print(today)

# COMMAND ----------

#dbutils.fs.mv("mnt/adls-curated/Dimension", f"mnt/adls-curated/Dimension_{today}", True)

# COMMAND ----------

for i in ListCurrentNotebooks():
    if i == CurrentNotebookPath():
        continue
    notebook = i.replace("/".join(CurrentNotebookPath().split("/")[:-1]), "").replace("/", "")
    print(notebook)
    try:
        spark.sql(f"DROP TABLE {DEFAULT_TARGET}.D_{notebook}")
    except:
        print(f"Bad {notebook}")
    print(notebook)

# COMMAND ----------

