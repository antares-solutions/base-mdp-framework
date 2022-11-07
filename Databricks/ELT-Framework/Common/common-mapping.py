# Databricks notebook source
# TODO: DEFINE HOW THIS MAPPING IS TO BE LOADED EITHER BY .CSV OR BY TABLE
def LoadMappings():
    return spark.sql("""
    SELECT 'trusted.dbo_extractloadmanifest' SourceTable, 'SourceTableName' Transformation, 'SourceTableName' TargetColumnName, 1 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, 'CONCAT(SourceTableName, SourceKeyVaultSecret)' Transformation, 'SourceTableNameConcat' TargetColumnName, 2 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, 'REPLACE(RawPath, \\'/\\', \\'\\')' Transformation, 'SourceTableNameConcat' TargetColumnName, 3 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, '1' Transformation, 'SomeInt' TargetColumnName, 4 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, '\\'ABC\\'' Transformation, 'SomeConstant' TargetColumnName, 5 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, 'DATE_FORMAT(CreatedDTS, \\'yyyyMMdd\\')' Transformation, 'DateFormatted' TargetColumnName, 6 Sequence
    UNION SELECT 'trusted.dbo_extractloadmanifest' SourceTable, 'SourceTableName' Transformation, 'Renamed' TargetColumnName, 7 Sequence
    """)

# COMMAND ----------

def TransformTable(tableName):
    # GET TABLE
    df = spark.table(tableName)
    
    # GET MAPPING
    mappingDf = LoadMappings().where(f"SourceTable = '{tableName}'")
    
    # EXIT IF NOT FOUND
    if mappingDf.count() == 0:
        print(f"No mapping found for: `{tableName}`!")
        return df
    
    # TRANSFORM
    transformedDf = df.selectExpr(
        [f"{i.Transformation} {i.TargetColumnName}" for i in mappingDf.orderBy("Sequence").rdd.collect()]
    )
    return transformedDf

# COMMAND ----------

def TransformTesting():
    # MAPPED
    df = TransformTable("trusted.dbo_extractloadmanifest")
    display(df)

    # MAPPING NOT HIT
    df = TransformTable("raw.dbo_extractloadmanifest")
    display(df)
#TransformTesting()

# COMMAND ----------