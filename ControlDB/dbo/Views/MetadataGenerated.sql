
CREATE  VIEW [dbo].[MetadataGenerated] AS
WITH [_Base] AS (
	SELECT
	[SystemCode],
	[ExtendedProperties],
	JSON_VALUE(T.value, '$.TABLE_SCHEMA') [TableSchema],
	JSON_VALUE(T.value, '$.TABLE_NAME') [TableName],
	JSON_VALUE(T.value, '$.COLUMN_NAME') [ColumnName],
	JSON_VALUE(T.value, '$.ORDINAL_POSITION') [OrdinalPosition],
	JSON_VALUE(T.value, '$.IS_NULLABLE') [IsNullable],
	JSON_VALUE(T.value, '$.DATA_TYPE') [DataType],
	JSON_VALUE(T.value, '$.CHARACTER_MAXIMUM_LENGTH') [CharacterMaximum_Length],
	JSON_VALUE(T.value, '$.NUMERIC_PRECISION') [NumericPrecision],
	JSON_VALUE(T.value, '$.NUMERIC_SCALE') [NumericScale]
	FROM [dbo].[ExtractLoadManifest] R
	CROSS APPLY OPENJSON ([SourceMetadata], N'$') T
	-- WHERE [SystemCode] IN ('EDW2'/*, 'EDW2', 'D365FO'*/)
)
, [_EXT] AS (
	SELECT 
    [SystemCode],
	[ExtendedProperties],
	[SourceSchema],
	[SourceTableName],
	JSON_VALUE(T.value, '$.SynapseTableSchema') [SynapseTableSchema],
	JSON_VALUE(T.value, '$.SynapseTableName') [SynapseTableName]
	FROM [dbo].[ExtractLoadManifest] R
	CROSS APPLY OPENJSON (concat('[',[ExtendedProperties],']'), N'$') T -- WHERE SourceID = '24052'
	)
,[_SourceQuery] AS (
	SELECT
	[SystemCode],
	[ExtendedProperties]
	,[TableSchema]
	,[TableName]
	,REPLACE(
	'BEGIN TRY DECLARE @Schema VARCHAR(8000) = REPLACE(''CREATE SCHEMA [$SS$]'', ''\\'', ''\'') EXEC(@Schema) END TRY BEGIN CATCH END CATCH '
	,'$SS$',MAX([TableSchema])) [CreateSchema]
	,REPLACE(
	'BEGIN TRY DECLARE @Schema VARCHAR(8000) = REPLACE(''CREATE SCHEMA [$ESS$]'', ''\\'', ''\'') EXEC(@Schema) END TRY BEGIN CATCH END CATCH '
	,'$ESS$',CASE WHEN [SystemCode] = 'D365FO' THEN 'D365' WHEN [SystemCode] IN ('EDW1','EDW2') THEN 'EDW' ELSE [SystemCode] END) [CreateExternalSchema]
	,REPLACE(REPLACE(REPLACE(
		CAST('CREATE TABLE [$SC$].[$TB$] ($C$)' AS NVARCHAR(MAX))
	,'$SC$', MAX([TableSchema]))
	,'$TB$', MAX([TableName]))
	,'$C$', STRING_AGG(
		REPLACE(REPLACE(REPLACE(REPLACE(
			CAST('[$C] [$D]$P $N' AS NVARCHAR(MAX))
		,'$C', [ColumnName])
		,'$D', [DataType])
		,'$N', IIF([IsNullable]='NO', 'NOT NULL','NULL'))
		,'$P',	CASE
					WHEN [DataType] LIKE '%char' OR [DataType] LIKE '%binary' THEN CONCAT('(', IIF([CharacterMaximum_Length]=-1, 'MAX', [CharacterMaximum_Length]), ')')
					WHEN [DataType] IN ('numeric', 'decimal') THEN CONCAT('(', [NumericPrecision], ',', [NumericScale], ')')
					WHEN [DataType] IN ('datetime2') THEN '(7)'
				ELSE '' END)
	,',')) [CreateTableSQL]
	,REPLACE(REPLACE(REPLACE(
		CAST('SELECT $C$ FROM [$SC$].[$TB$] ' AS NVARCHAR(MAX))
	,'$SC$', MAX([TableSchema]))
	,'$TB$', MAX([TableName]))
	,'$C$', STRING_AGG(
		REPLACE(REPLACE(
			CAST('[$C] [$R]' AS NVARCHAR(MAX))
		,'$C', [ColumnName])
		,'$R', REPLACE(REPLACE(REPLACE(REPLACE(
			[ColumnName]
			, ' ', '_')
			, ',', '_')
			, '(', '_')
			, ')', '_')
		)
	,',')) [SelectSQL]
	FROM [_Base]
	GROUP BY
	[SystemCode]
	,[ExtendedProperties]
	,[TableSchema]
	,[TableName]
)
,[_GeneratedQueries] AS (
	SELECT 
	A.*, iif(isnull(len(A.[ExtendedProperties]),0) < 1,
		REPLACE(REPLACE(REPLACE(
		CONCAT(A.[CreateTableSQL], CONCAT(' WITH (LOCATION =''/external-tables/', A.[SystemCode], '/', A.[TableSchema], '_', A.[TableName], '/'' ,DATA_SOURCE = [DLS-Synapse-EDS], ', 'FILE_FORMAT = [SynapseParquetFormat] )'))
	,'CREATE TABLE', 'CREATE EXTERNAL TABLE')
	,CONCAT('[', A.[TableName], ']'), CONCAT('[ext_', A.[TableName], ']'))
	,CONCAT('[', A.[TableSchema], ']'), CONCAT('[', CASE WHEN A.[SystemCode] = 'D365FO' THEN 'D365' WHEN A.[SystemCode] IN ('EDW1','EDW2') THEN 'EDW' ELSE A.[SystemCode] END, ']')),
		REPLACE(REPLACE(REPLACE(
		CONCAT(A.[CreateTableSQL], CONCAT(' WITH (LOCATION =''/external-tables/', A.[SystemCode], '/', A.[TableSchema], '_', A.[TableName], '/'' ,DATA_SOURCE = [DLS-Synapse-EDS], ', 'FILE_FORMAT = [SynapseParquetFormat] )'))
	,'CREATE TABLE', 'CREATE EXTERNAL TABLE')
	,CONCAT('[', A.[TableName], ']'), CONCAT('[ext_', B.[SynapseTableName], ']'))
	,CONCAT('[', A.[TableSchema], ']'), CONCAT('[', B.[SynapseTableSchema], ']'))
	) CreateExternalTableSQL
	FROM [_SourceQuery] A LEFT JOIN [_EXT] B ON (A.SystemCode = B.SystemCode and A.TableSchema = B.SourceSchema and A.TableName = B.SourceTableName)
)

SELECT * FROM [_GeneratedQueries]

GO


