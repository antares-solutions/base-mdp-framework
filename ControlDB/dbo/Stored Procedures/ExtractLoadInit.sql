

CREATE PROCEDURE [dbo].[ExtractLoadInit] 
	@BatchID VARCHAR(MAX),
	@SystemCode VARCHAR(MAX)
AS
BEGIN

BEGIN
	WITH [LastWatermark] AS (
		SELECT [SourceID], [HighWatermark] FROM (
			SELECT 
			[SourceID]
			,[HighWatermark]
			,RANK() OVER (PARTITION BY [SourceID] ORDER BY [CreatedDTS] DESC) [Rank]
			FROM [dbo].[ExtractLoadStatus]
			WHERE [HighWatermark] IS NOT NULL
		) T WHERE [Rank] = 1
	)
	INSERT INTO [dbo].[ExtractLoadStatus] (
	[BatchID]
	,[SystemCode]
	,[SourceID]
	,[LowWatermark]
    ,[HighWatermark]
	,[SourceRowCount]
	,[SinkRowCount]
	,[RawPath]
	,[RawStatus]
	,[RawStartDTS]
	,[RawEndDTS]
	,[CreatedDTS])
	SELECT 
	@BatchID [BatchID]
	,@SystemCode [SystemCode]
	,S.[SourceID]
	,W.[HighWatermark] [LowWatermark] /*LOAD PREVIOUS */
	,NULL [HighWatermark]
	,NULL [SourceRowCount]
	,NULL [SinkRowCount]
	,NULL [RawPath]
	,NULL [RawStatus]
	,NULL [RawStartDTS]
	,NULL [RawEndDTS] 
	,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time') [CreatedDTS]
	FROM [dbo].[ExtractLoadManifest] S
	LEFT JOIN [LastWatermark] W ON W.SourceID = S.SourceID 
	WHERE SystemCode = @SystemCode
	AND S.[Enabled] = 1
END

BEGIN
	SELECT S.BatchID, S.ID, S.LowWatermark
	,R.[SourceID]
    ,R.[SystemCode]
    ,[SourceSchema]
    ,[SourceTableName]
    ,[SourceQuery]
    ,[SourceFolderPath]
    ,[SourceFileName]
    ,[SourceKeyVaultSecret]
    ,[SourceHandler]
    ,[LoadType]
    ,[BusinessKeyColumn]
    ,[WatermarkColumn]
    ,[RawHandler]
    ,R.[RawPath]
    ,[TrustedHandler]
    ,[TrustedPath]
    ,[DestinationSchema]
    ,[DestinationTableName]
    ,[DestinationKeyVaultSecret]
    ,[ExtendedProperties]
	FROM [dbo].[ExtractLoadStatus] S
	JOIN [dbo].[ExtractLoadManifest] R ON R.SourceID = S.SourceID
	WHERE 
	S.BatchID = @BatchID
	AND S.SystemCode = @SystemCode
	AND R.[Enabled] = 1
END

END
GO
