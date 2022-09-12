# Databricks notebook source
import requests
import json
from ast import literal_eval

# COMMAND ----------

def ListNotebooks(instanceName,loc="/"):
    PAT = dbutils.secrets.get(scope = "secret-scope", key = "Databricks-PAT")
    headers = {
        'Authorization': f'Bearer {PAT}',
    }
    data_path = '{{"path": "{0}"}}'.format(loc)
    instance = instanceName
    url = '{}/api/2.0/workspace/list'.format(instance)
    response = requests.get(url, headers=headers, data=data_path)

    response.raise_for_status()
    jsonResponse = response.json()
    list = []
    for i,result in jsonResponse.items():
        for value in result:
            dump = json.dumps(value)
            data = literal_eval(dump)
            if data['object_type'] == 'DIRECTORY':
                rec_req(instanceName,data['path'])
            elif data['object_type'] == 'NOTEBOOK':
                 list.append(data['path'])
    else:
        pass
    return list

# COMMAND ----------

def ListCurrentNotebooks():
    path = "/".join(CurrentNotebookPath().split("/")[:-1])
    return ListNotebooks("https://australiaeast.azuredatabricks.net", path)

# COMMAND ----------

def CurrentNotebookPath():
    return dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# COMMAND ----------

