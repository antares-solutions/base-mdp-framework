# Databricks notebook source
# MAGIC %run ./common-class

# COMMAND ----------

# MAGIC %run ./common-scd

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import *
from datetime import *
import pytz

# COMMAND ----------

DEFAULT_SOURCE = "trusted"
DEFAULT_TARGET = "curated"
DEFAULT_START_DATE = "NOW()"
DEFAULT_END_DATE = "NULL"

DEBUG = 0
FLAGS = 0

# COMMAND ----------

#OVERRIDE DEFAULTS BY PARAMETERS
print(f"Defaults: Source={DEFAULT_SOURCE} Target={DEFAULT_TARGET} Start={DEFAULT_START_DATE} End={DEFAULT_END_DATE}")
try:
    DEFAULT_SOURCE = dbutils.widgets.get("default_source")
    DEFAULT_TARGET = dbutils.widgets.get("default_target")
    DEFAULT_START_DATE = dbutils.widgets.get("default_start_date")
    DEFAULT_END_DATE =  dbutils.widgets.get("default_end_date")
    print(f"Overwritten defaults: Source={DEFAULT_SOURCE} Target={DEFAULT_TARGET} Start={DEFAULT_START_DATE} End={DEFAULT_END_DATE}")
except:
    pass

# COMMAND ----------

class CuratedTransform( BlankClass ):
  Counts = BlankClass()
  
  def __init__(self):
      list = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split("/")
      count=len(list)
      self.EntityType = list[count-2]
      self.Name = list[count-1]
      self.EntityName = f"{self.EntityType[0:1]}_{self.Name}"
      self.Destination = f"{DEFAULT_TARGET}.{self.EntityName}"
      self.DataLakePath = f"/mnt/adls-{DEFAULT_TARGET}/{self.EntityType}/{self.EntityName}"
      self.Tables = []
      #self.Joins = []
  
  def _NotebookEnd(self):
    r = json.dumps(
      {
        "Counts" : self.Counts.__dict__,
        "CuratedTransform" : self.__dict__
      })
    dbutils.notebook.exit(r)
  pass

# COMMAND ----------

_ = CuratedTransform()

# COMMAND ----------

def TableExists(tableFqn):
  return spark._jsparkSession.catalog().tableExists(tableFqn.split(".")[0], tableFqn.split(".")[1])

# COMMAND ----------

def GetTable(tableFqn):
    _.Tables.append(tableFqn) if tableFqn not in _.Tables else _.Tables
    return spark.table(tableFqn).cache()

# COMMAND ----------

def GetCurrentTable(tableFqn):
    return GetTable(tableFqn).where(expr("_current = 1"))

# COMMAND ----------

def _InjectSK(dataFrame):
  skName = f"{_.Name}_SK"
  lastMax = (spark.table(_.Destination).agg({skName : "max"}).collect()[0][0]) if TableExists(_.Destination) else 0
  df = dataFrame
  df = df.withColumn(skName, expr(f"CONCAT(date_format(now(), 'yyMMddHHmmss'), '-', {_.Name}_BK)"))
  #HASH THIS COLUMN AS INT

  columns = [c for c in dataFrame.columns]
  columns.insert(0, skName)
  df = df.select(columns)

  return df

# COMMAND ----------

def _AddSCD(dataFrame):
  df = dataFrame
  df = df.withColumn("_Created", expr(f"CAST({DEFAULT_START_DATE} AS TIMESTAMP)"))
  df = df.withColumn("_Ended", expr("CAST(NULL AS TIMESTAMP)" if DEFAULT_END_DATE == "NULL" else f"CAST(({DEFAULT_END_DATE} + INTERVAL 1 DAY) - INTERVAL 1 SECOND AS TIMESTAMP)"))
  df = df.withColumn("_Current", expr("CAST(1 AS INT)"))
  return df

# COMMAND ----------

def IsDimension():
  return _.EntityType == "Dimension"

# COMMAND ----------

def _WrapSystemColumns(dataFrame):
  return _AddSCD(_InjectSK(dataFrame))

# COMMAND ----------

def GetTableRowCount(tableFqn):
  return spark.table(tableFqn).count() if TableExists(tableFqn) else 0

# COMMAND ----------

def SaveDelta(dataFrame):
    targetTableFqn = _.Destination
    dataLakePath = _.DataLakePath
    CreateDeltaTable(dataFrame, targetTableFqn, dataLakePath)

# COMMAND ----------

def Overwrite(dataFrame):
    CleanTable(_.Destination)
    CreateDeltaTable(dataFrame, _.Destination, _.DataLakePath)
    EndNotebook(dataFrame)

# COMMAND ----------

def CleanSelf():
    try:
        CleanTable(_.Destination)
    except:
        pass

# COMMAND ----------

def _ValidateBK(sourceDataFrame):
    print(f"Validating {_.Name}_BK...")
    dupesDf = sourceDataFrame.groupBy(f"{_.Name}_BK").count() \
      .withColumnRenamed("count", "n") \
      .where("n > 1") 
    
    if (dupesDf.count() > 1):
        print(f"WARNING! THERE ARE DUPES ON {_.Name}_BK!")       
        dupesDf.show()

# COMMAND ----------

def Save(sourceDataFrame):
  targetTableFqn = f"{_.Destination}"
  print(f"Saving {targetTableFqn}...")
  sourceDataFrame = _WrapSystemColumns(sourceDataFrame) if sourceDataFrame is not None else None

  if (not(TableExists(targetTableFqn))):
    print(f"Creating {targetTableFqn}...")
    CreateDeltaTable(sourceDataFrame, targetTableFqn, _.DataLakePath)  
    EndNotebook(sourceDataFrame)
    return

  #if not(IsDimension()):
    #AppendDeltaTable(sourceDataFrame, _.Destination, _.DataLakePath)
    #EndNotebook(sourceDataFrame)
    #return
  
  targetTable = spark.table(targetTableFqn)
  
  _exclude = {f"{_.Name}_SK", f"{_.Name}_BK", '_Created', '_Ended', '_Current'}
  changeColumns = " OR ".join([f"s.{c} <> t.{c}" for c in targetTable.columns if c not in _exclude])
  
  newRecords = sourceDataFrame.alias("s") \
    .join(targetTable.alias("t"), f"{_.Name}_BK") \
    .where(f"t._Current = 1 AND ({changeColumns})")

  stagedUpdates = newRecords.selectExpr("NULL BK", "s.*") \
    .union( \
      sourceDataFrame.selectExpr(f"{_.Name}_BK BK", "*") \
    )
  
  insertValues = {
        f"{_.Name}_SK": f"s.{_.Name}_SK",
        f"{_.Name}_BK": f"s.{_.Name}_BK",
        "_Created": "s._Created",
        "_Ended": DEFAULT_END_DATE,
        "_Current": "1"
    }
  for c in [i for i in targetTable.columns if i not in _exclude]:
    insertValues[f"{c}"] = f"s.{c}"
  
  DeltaTable.forName(spark, targetTableFqn).alias("t").merge(stagedUpdates.alias("s"), f"t.{_.Name}_BK = BK") \
    .whenMatchedUpdate(
      condition = f"t._Current = 1 AND ({changeColumns})", 
      set = {
        #"_Ended": expr("now()"),
        "_Ended": expr(f"{DEFAULT_START_DATE} - INTERVAL 1 SECOND"),
        "_Current": "0"
      }
    ) \
    .whenNotMatchedInsert(
      values = insertValues
    ).execute()
  
  EndNotebook(sourceDataFrame)
  return 

# COMMAND ----------

def Update(sourceDataFrame):
    targetTableFqn = f"{_.Destination}"
    dt = DeltaTable.forName(spark, targetTableFqn)
    _exclude = {f"{_.Name}_SK", f"{_.Name}_BK", '_Created', '_Ended', '_Current'}
    targetTable = spark.table(targetTableFqn)
    updates = {
    }
    for c in [i for i in targetTable.columns if i not in _exclude]:
        updates[f"{c}"] = f"s.{c}"
    
    dt.alias("t").merge(
        sourceDataFrame.alias("s")
        ,f"t.{_.Name}_BK = s.{_.Name}_BK"
        ) \
        .whenMatchedUpdate(
        set = updates
        ).execute()
    EndNotebook(sourceDataFrame)

# COMMAND ----------

def EndNotebook(df):
  if not(DEBUG):
    _.Counts.SpotCount = df.count() if df is not None else 0
    _.Counts.InsertCount = -1#GetRandomNumber() #TODO
    _.Counts.UpdateCount = -1#GetRandomNumber() #TODO
    _.Counts.CuratedCount = GetTableRowCount(_.Destination)
  else:
    _.Columns = [c for c in sourceDataFrame.columns] if df is not None else None
  
  _._NotebookEnd() if FLAGS==0 else display(spark.table(_.Destination))

# COMMAND ----------

def UnioniseQuery(query):
    df = None
    for i in {"", "nz"}:
        id = 1 if i=="" else 2
        c = "" if i=="" else "_nz"
        localDf = spark.sql(query.replace(f"{DEFAULT_SOURCE}.dbo", f"{DEFAULT_SOURCE}.dbo{c}")).withColumn("Organisation", lit(id))

        if df == None:
            df = localDf
        else:
            df = df.unionAll(localDf)
    return df
