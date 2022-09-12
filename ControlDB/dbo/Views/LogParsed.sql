
CREATE VIEW [dbo].[LogParsed] AS
WITH [Main] AS (
SELECT --TOP 10
[ID]
,[ExtractLoadStatusID]
,[ActivityType]
,REPLACE(REPLACE([Message], CHAR(13), ''), CHAR(10), '') [Message]
,[CreatedDTS]
FROM [dbo].[Log] (NOLOCK)
)
SELECT 
* 
,JSON_VALUE([Message],'$.PipelineRunId') [JsonPipelineRunId]
,JSON_VALUE([Message],'$.Status') [Status]
,FORMAT((CAST(JSON_VALUE([Message],'$.dataRead') AS DECIMAL(16, 2)) / (1024 ^ 2)), '0.00')  [DataRead]
,FORMAT((CAST(JSON_VALUE([Message],'$.dataWritten') AS DECIMAL(16, 2)) / (1024 ^ 2)), '0.00')  [DataWritten]
,FORMAT((CAST(JSON_VALUE([Message],'$.rowsRead') AS INT)), '')  [RowsRead]
,FORMAT((CAST(JSON_VALUE([Message],'$.rowsCopied') AS INT)), '')  [RowsCopied]
,FORMAT((CAST(JSON_VALUE([Message],'$.copyDuration') AS INT)), '')  [CopyDuration]
,FORMAT((CAST(JSON_VALUE([Message],'$.throughput') AS DECIMAL(16, 2))), '0.00')  [Throughput]
,IIF(JSON_VALUE([Message],'$.Output.errors[0].Message') IS NOT NULL, JSON_VALUE([Message],'$.Output.errors[0].Message'), JSON_VALUE([Message],'$.Error.message')) [Error]
FROM [Main]
GO