# Databricks notebook source
# MAGIC %run ../Common/common-include-all

# COMMAND ----------

task = dbutils.widgets.get("task")
rawPath = dbutils.widgets.get("rawPath").replace("/raw", "/mnt/adls-raw")

# COMMAND ----------

j = json.loads(task)

schemaName = j.get("DestinationSchema")
tableName = j.get("DestinationTableName")
rawTargetPath = j.get("RawPath")
rawFolderPath = "/".join(rawPath.split("/")[0:-1])

fileFormat = ""
fileOptions = ""

if("xml" in rawTargetPath):
    extendedProperties = json.loads(j.get("ExtendedProperties"))
    rowTag = extendedProperties.get("rowTag")
    fileFormat = "XML"
    fileOptions = f", rowTag \"{rowTag}\""
elif ("csv" in rawTargetPath):
    fileFormat = "CSV"
    fileOptions = ", header \"true\", inferSchema \"true\", multiline \"true\""
elif ("json" in rawTargetPath):
    fileFormat = "JSON"
    fileOptions = ", multiline \"true\", inferSchema \"true\""
else:
    fileFormat = "PARQUET"

# COMMAND ----------

tableFqn = f"raw.{schemaName}_{tableName}"
sql = f"DROP TABLE IF EXISTS {tableFqn};"
spark.sql(sql)
sql = f"CREATE TABLE {tableFqn} USING {fileFormat} OPTIONS (path \"{rawFolderPath}\" {fileOptions});"
spark.sql(sql)

print(spark.table(f"{tableFqn}").count())