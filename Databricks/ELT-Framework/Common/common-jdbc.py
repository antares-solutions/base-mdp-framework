# Databricks notebook source
def ExecuteJDBCQuery(sql, targetJdbcKVSecretName):
  jdbc = GetJdbc(targetJdbcKVSecretName)
  connection = spark._sc._gateway.jvm.java.sql.DriverManager.getConnection(jdbc)
  connection.prepareCall(sql).execute()
  connection.close()

def WriteTable(sourceTable, targetTable, mode, jdbc):
  df = spark.table(sourceTable)
  df.write \
  .mode(mode) \
  .jdbc(jdbc, targetTable)

def GetJdbc(jdbcKVSecret):
  return dbutils.secrets.get(scope = "secret-scope", key = jdbcKVSecret)

def AppendTable(sourceTable, targetTable, targetJdbcKVSecretName):
  jdbc = GetJdbc(targetJdbcKVSecretName)
  WriteTable(sourceTable, targetTable, "append", jdbc)
  
def WriteSynapseTable(sourceDataFrame, targetTable, mode="overwrite"):
    accessKey = GetStorageKey()
    jdbc = GetSynapseJdbc()
    dataLakeName = GetDataLakeFqn().split(".")[0]
    blobFqn = f"{dataLakeName}.blob.core.windows.net"

    tempDir = f"wasbs://synapse@{blobFqn}/tempDirs"
    acntInfo = f"fs.azure.account.key.{blobFqn}"
    sc._jsc.hadoopConfiguration().set(acntInfo, accessKey)
    spark.conf.set("spark.sql.parquet.writeLegacyFormat", "true")

    sourceDataFrame.write.format("com.databricks.spark.sqldw") \
    .option("url", jdbc) \
    .option("dbtable", targetTable) \
    .option("forward_spark_azure_storage_credentials", "True") \
    .option("tempdir", tempDir) \
    .mode(mode).save()

def CreateSqlTableFromSource(sourceTable, targetTable, targetJdbcKVSecretName):
    jdbc = GetJdbc(targetJdbcKVSecretName)
    sql = f"CREATE TABLE {targetTable} \
                USING org.apache.spark.sql.jdbc \
                OPTIONS ( \
                  url \"{jdbc}\", \
                  dbtable \"{sourceTable}\" \
                )"
    spark.sql(sql)
    
def GetSqlDataFrame(tableFqn, targetJdbcKVSecretName):
    jdbc = GetJdbc(targetJdbcKVSecretName)
    return spark.read.option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver").jdbc(url=jdbc, table=tableFqn)

# COMMAND ----------

