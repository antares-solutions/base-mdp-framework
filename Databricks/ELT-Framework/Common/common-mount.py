# Databricks notebook source
def MountExists(containerName):
  return any( containerName in mount.mountPoint for mount in dbutils.fs.mounts())

# COMMAND ----------

def MountContainer(containerName):
  if(MountExists(containerName)):
    return
  
  SECRET_SCOPE = "secret-scope"
  APP_ID = dbutils.secrets.get(scope = SECRET_SCOPE, key = "Service-Principal-ApplicationID")
  SECRET = dbutils.secrets.get(scope = SECRET_SCOPE, key = "Service-Principal-Secret")
  DIRECTORY_ID = dbutils.secrets.get(scope = SECRET_SCOPE, key = "TenantID")
  configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": APP_ID,
           "fs.azure.account.oauth2.client.secret": SECRET,
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/{0}/oauth2/token".format(DIRECTORY_ID)}
  dlFqn = dbutils.secrets.get(scope = SECRET_SCOPE, key = "DL-FQN")
  
  DATA_LAKE_SOURCE = f"abfss://{containerName}@{dlFqn}/"
  MOUNT_POINT = f"/mnt/adls-{containerName}"
  dbutils.fs.mount(
        source = DATA_LAKE_SOURCE,
        mount_point = MOUNT_POINT,
        extra_configs = configs)
  spark.sql(f"CREATE DATABASE {containerName}")

# COMMAND ----------

MountContainer("raw")
MountContainer("trusted")
MountContainer("curated")
