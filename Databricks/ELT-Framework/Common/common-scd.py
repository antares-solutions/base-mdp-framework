# Databricks notebook source
from delta.tables import *

# COMMAND ----------

# MAGIC %run ./common-spark

# COMMAND ----------

def PrefixColumn(columns, prefix=None):
  return ",".join([f"{prefix}.{k}" for k in columns.split(',')]) if(',' in columns) else f"{prefix}.{columns}"

# COMMAND ----------

def ConcatBusinessKey(columns, prefix=None):
  p = PrefixColumn(columns, prefix)
  return f"CONCAT({p})" if(',' in columns) else p

# COMMAND ----------

def BasicMerge(sourceDataFrame, targetTableFqn, businessKey=None):
  businessKey = spark.table(targetTableFqn).columns[0] if businessKey is None else businessKey
  s = ConcatBusinessKey(businessKey, "s")
  t = ConcatBusinessKey(businessKey, "t")
  
  df = DeltaTable.forName(spark, targetTableFqn).alias("t").merge(sourceDataFrame.alias("s"), f"{s} = {t}") \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute()

# COMMAND ----------

def CreateOrMerge(sourceDataFrame, targetTableFqn, dataLakePath, businessKey=None):
  if (TableExists(targetTableFqn)):
    BasicMerge(sourceDataFrame, targetTableFqn, businessKey)
  else:
    CreateDeltaTable(sourceDataFrame, targetTableFqn, dataLakePath)  