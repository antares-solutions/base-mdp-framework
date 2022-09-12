# Databricks notebook source
# MAGIC %run ../../Common/common-transform

# COMMAND ----------

def CreateDatabase(database):
    print(database)
    try:
        spark.sql(f"DROP DATABASE {database} CASCADE")
    except:
        pass
    
    spark.sql(f"CREATE DATABASE {database}")

# COMMAND ----------

def MountFusion():
    fileOptions = ", header \"true\", inferSchema \"true\", multiline \"true\""

    for i in dbutils.fs.ls(f"/mnt/adls-raw/HistoricFusion/AUS/{asAtDate}"):
        file = i.name.replace(".csv", "")
        rawFolderPath = i.path.replace("dbfs:", "")
        table = f"fusion.dbo_{file}"
        nzTable = f"fusion.dbo_nz_{file}"
        count = spark.read.option("header", "true").csv(rawFolderPath).count()

        if count == 0:
            continue
        if TableExists(table):
            spark.sql(f"DROP TABLE {table}")
        sql = f"CREATE TABLE {table} USING CSV OPTIONS (path \"{rawFolderPath}\" {fileOptions});"
        print(sql)
        spark.sql(sql)
        try:
            sql = f"CREATE VIEW {nzTable} AS SELECT * FROM {table} LIMIT 0"
            #spark.sql(sql)
        except:
            pass
        #break
#MountFusion()

# COMMAND ----------

def LoadDeltaCopy():
    for i in dbutils.fs.ls("mnt/adls-history/Fact"):
        #print(i)
        targetTableFqn = f"history.{i.name}".replace("/", "")
        dataLakePath = i.path
        sql = f"CREATE TABLE IF NOT EXISTS {targetTableFqn} USING DELTA LOCATION \'{dataLakePath}\'"
        print(sql)
        spark.sql(sql)

# COMMAND ----------

def MountFusionFilled(database, asAtDate):
    CreateDatabase(database)
    fileOptions = ", header \"true\", inferSchema \"true\", multiline \"true\""

    for i in dbutils.fs.ls(f"/mnt/adls-raw/HistoricFusion/AUS/{asAtDate}"):
        file = i.name.replace(".csv", "")
        rawFolderPath = i.path.replace("dbfs:", "")
        table = f"dbo_{file}"
        tableFqn = f"{database}.{table}"
        count = spark.read.option("header", "true").csv(rawFolderPath).count()
        #print(table)
        
        if count == 0:
            continue
        if (TableExists(f"raw.{table}")==False):
            continue
        #if TableExists(tableFqn):
            #spark.sql(f"DROP TABLE {tableFqn}")

        df = spark.read.format("csv") \
            .option("header", "true") \
            .option("multiline", "true") \
            .option("quote", "\"") \
            .schema(spark.table(f"raw.{table}").schema) \
            .load(rawFolderPath) \
            .na.fill("") \
            .write.mode("overwrite").saveAsTable(tableFqn) 
        #display(df)
            
        #try:
        sql = f"CREATE OR REPLACE VIEW {database}.dbo_nz_{file} AS SELECT * FROM {tableFqn} LIMIT 0"
        spark.sql(sql)
        #except:
            #pass
        #break

# COMMAND ----------

def RunNotebooks(source, target, startDate, endDate):
    #CreateDatabase(target)
    df = spark.sql(f"SHOW TABLES FROM {target}").select("tableName").rdd.collect()
    list = [i.tableName for i in df]

    df = spark.sql("SELECT * FROM transformmanifest ORDER BY TransformID")

    for i in df.rdd.collect():
        table = i.EntityName
        #print(table)
        
        if table not in ["f_revenue"]:
            continue

        # IGNORE THESE OR THE ONES ALREADY PROCESSED
        if(table in {"d_organisation", "d_fulldatecalendar", "d_asatdate", "d_exchangerate", "d_date", "f_factlesssalesperioddate", "f_payments", "f_organisationpayment", "f_organisationcontractassociated"} or "f_manual" in table 
           #or table in list
          ):
            continue
            
        path = f"../../{i.Command}"
        print(path)

        try:
            dbutils.notebook.run(path, 0, { "default_source" : source, "default_target" : target , "default_start_date" : f"'{startDate}'", "default_end_date" : f"'{endDate}'" })
        except:
            pass
        #break

# COMMAND ----------

from datetime import *

def HistoryLoad():
    asAtDates = [20201227, 20210103]
    #asAtDates = [20211226, 20220410]
    
    for asAtDate in asAtDates:
        endDate = datetime.strptime(str(asAtDate), '%Y%m%d')
        startDate = endDate - timedelta(6)
        source = f"fusion_{asAtDate}"
        target = f"history"
        #target = f"history_{asAtDate}"
        #MountFusionFilled(source, asAtDate)
        RunNotebooks(source, target, startDate, endDate)
#HistoryLoad()

# COMMAND ----------


