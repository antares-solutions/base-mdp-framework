CREATE VIEW [dbo].[ObjectLineage] AS 
WITH [_Log] AS (
	SELECT
	[ID]
	,[ActivityType]
	,REPLACE(REPLACE([Message], CHAR(13), ''), CHAR(10), '') [Message]
	FROM [dbo].[Log] (NOLOCK)
	WHERE [TransformStatusID] IS NOT NULL
)
, [_ReportLineage] AS (
	SELECT
	[ReportName]
	,[SourceTable]
	FROM (
		SELECT [ReportName]
		,[SourceTable]
		,RANK() OVER (PARTITION BY [ReportName] ORDER BY [CreatedDTS] DESC) [Rank]
		FROM [dbo].[ReportRefreshStatus]
	) T
	WHERE [Rank] = 1
) 
,[_CuratedLineage] AS (
	SELECT 
	DISTINCT 
	R.ReportName [ReportName]
	,R.SourceTable [CuratedDestination]
	,L.value [SourceTable]
	FROM [_Log]
	CROSS APPLY OPENJSON ([Message], N'$.Output.runOutput.CuratedTransform.Tables') L
	JOIN [_ReportLineage] R ON R.SourceTable = JSON_VALUE([Message], '$.Output.runOutput.CuratedTransform.Destination')
)
,[_TransformManifest] AS (
	SELECT [TransformID]
	,REPLACE(
	'curated.$T$'
	,'$T$', LOWER([EntityName])) [CuratedTable]
	FROM [dbo].[TransformManifest]
)
,[_TrustedLineage] AS (
	SELECT  
	[SystemCode]
	,[SourceID]
	,REPLACE(REPLACE(
	'trusted.$S$_$T$'
	,'$S$', [DestinationSchema])
	,'$T$', [DestinationTableName]) [TrustedTable]
	FROM [dbo].[ExtractLoadManifest]
)
SELECT 
[ReportName]
,[TransformID]
,[CuratedTable]
,[SourceID]
,[TrustedTable]

FROM [_CuratedLineage] C
JOIN [_TransformManifest] TM ON TM.CuratedTable = C.[CuratedDestination]
JOIN [_TrustedLineage] T ON T.[TrustedTable] = C.SourceTable
GO