# Databricks notebook source
def GetSecret(secretName):
    return dbutils.secrets.get(SECRET_SCOPE, secretName)
  
def GetStorageKey():
    return GetSecret(DATA_LAKE_KEY_SECRET_NAME)

def GetSynapseJdbc():
    return GetSecret(SYNAPSE_JDBC_SECRET_NAME)

def GetDataLakeFqn():
    return GetSecret(DATA_LAKE_FQN)