
CREATE VIEW [dbo].[HealthDashboard] AS
WITH [_BatchLog] AS (
SELECT
*
FROM [dbo].[BatchStatusLog]
)
SELECT 
B.*
--,[SourceSchema]
--,[SourceTableName]
,L.[TransformID]
,[CuratedTable]
,L.[ReportName]
,[BatchEndDTS] [LastRun]
,CAST(CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time')-[BatchEndDTS] AS TIME) [NextRefresh]
,(CAST([BatchSuccessTasks]-1 AS DECIMAL(6, 3)) / CAST([BatchTotalTasks] AS DECIMAL(6, 3)))  [SuccessRate]
,CONCAT('Q', DATEPART(QUARTER, [RawStartDTS])) [Period]
--,IIF(B.BatchID = '65d167f1', 1, 0) [Latest]
,[LatestBatch] [Latest]

FROM [_BatchLog] B
JOIN [dbo].[ObjectLineage] L ON L.SourceID = B.SourceID
JOIN [dbo].[TransformManifest] T ON T.TransformID = L.TransformID
JOIN [dbo].[ExtractLoadManifest] E ON E.SourceID = B.SourceID
--JOIN [dbo].[ReportRefreshStatus] R ON R.SourceTable = CuratedTable
GO

