

CREATE PROCEDURE [dbo].[TransformInit] 
	@BatchID VARCHAR(MAX)
AS
BEGIN

BEGIN
	
	INSERT INTO [dbo].[TransformStatus] (
	[BatchID]
    ,[TransformID]
	,[CreatedDTS])
	SELECT 
	@BatchID [BatchID]
	,M.[TransformID]
	,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time') [CreatedDTS]
	FROM [dbo].[TransformManifest] M
	WHERE M.[Enabled] = 1
END

BEGIN
	SELECT 
	S.BatchID
	,S.ID
	,M.*
	,(SELECT STRING_AGG([ParallelGroup], ',') [List] FROM (SELECT DISTINCT TOP 100 PERCENT [ParallelGroup] FROM [dbo].[TransformManifest] ORDER BY [ParallelGroup]) T) [List]
	FROM [dbo].[TransformStatus] S
	JOIN [dbo].[TransformManifest] M ON M.[TransformID] = S.[TransformID]
	WHERE 
	S.BatchID = @BatchID
	AND M.[Enabled] = 1
END

END
GO