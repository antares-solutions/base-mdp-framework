# Databricks notebook source
# MAGIC %run ../Common/common-include-all

# COMMAND ----------

spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "CORRECTED")
spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "CORRECTED")
task = dbutils.widgets.get("task")
j = json.loads(task)
systemCode = j.get("SystemCode")
destinationSchema = j.get("DestinationSchema")
destinationTableName = j.get("DestinationTableName")
trustedPath = j.get("TrustedPath")
businessKey = j.get("BusinessKeyColumn")
destinationKeyVaultSecret = j.get("DestinationKeyVaultSecret")
extendedProperties = j.get("ExtendedProperties")
dataLakePath = trustedPath.replace("/trusted", "/mnt/adls-trusted")
sourceTableName = f"raw.{destinationSchema}_{destinationTableName}"

# COMMAND ----------

sourceDataFrame = spark.table(sourceTableName)

#FIX BAD COLUMNS
sourceDataFrame = sourceDataFrame.toDF(*(c.replace(' ', '_') for c in sourceDataFrame.columns))

#TRUSTED QUERY FROM RAW TO FLATTEN OBJECT
if(extendedProperties):
  extendedProperties = json.loads(extendedProperties)
  trustedQuery = extendedProperties.get("TrustedQuery")
  if(trustedQuery):
    sourceDataFrame = spark.sql(trustedQuery.replace("{tableFqn}", sourceTableName))

tableName = f"{destinationSchema}_{destinationTableName}"
CreateDeltaTable(sourceDataFrame, f"trusted.{tableName}", dataLakePath) if j.get("BusinessKeyColumn") is None else CreateOrMerge(sourceDataFrame, f"trusted.{tableName}", dataLakePath, j.get("BusinessKeyColumn"))

# COMMAND ----------

