# Databricks notebook source
def TableExists(tableFqn):
  return spark._jsparkSession.catalog().tableExists(tableFqn.split(".")[0], tableFqn.split(".")[1])

# COMMAND ----------

def GetDeltaTablePath(tableFqn):
  df = spark.sql(f"DESCRIBE TABLE EXTENDED {tableFqn}").where("col_name = 'Location'")
  return df.rdd.collect()[0].data_type

# COMMAND ----------

def CreateDeltaTable(dataFrame, targetTableFqn, dataLakePath):
  dataFrame.write \
    .format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .save(dataLakePath)
  spark.sql(f"CREATE TABLE IF NOT EXISTS {targetTableFqn} USING DELTA LOCATION \'{dataLakePath}\'")

# COMMAND ----------

def AppendDeltaTable(dataFrame, targetTableFqn, dataLakePath):
  dataFrame.write \
    .format("delta") \
    .option("mergeSchema", "true") \
    .mode("append") \
    .save(dataLakePath)
  if (not(TableExists(targetTableFqn))):
    spark.sql(f"CREATE TABLE IF NOT EXISTS {targetTableFqn} USING DELTA LOCATION \'{dataLakePath}\'")

# COMMAND ----------

def AliasDataFrameColumns(dataFrame, prefix):
  return dataFrame.select(*(col(x).alias(prefix + x) for x in dataFrame.columns))

# COMMAND ----------

def CleanTable(tableNameFqn):
    try:
        detail = spark.sql(f"DESCRIBE DETAIL {tableNameFqn}").rdd.collect()[0]
        dbutils.fs.rm(detail.location, True)
        spark.sql(f"DROP TABLE {tableNameFqn}")
    except:    
        pass

# COMMAND ----------

