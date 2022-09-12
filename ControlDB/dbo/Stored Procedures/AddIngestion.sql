CREATE PROCEDURE [dbo].[AddIngestion] 
	@SystemCode VARCHAR(MAX),
	@Schema VARCHAR(MAX),
	@Table VARCHAR(MAX),
	@Query VARCHAR(MAX),
	@WatermarkColumn VARCHAR(MAX),
	@SourceHandler VARCHAR(MAX),
	@RawFileExtension VARCHAR(MAX),
	@KeyVaultSecret VARCHAR(MAX),
	@ExtendedProperties VARCHAR(MAX)
AS
BEGIN

/* TODO: UPDATE EXISTING CONFIGURATION */
IF (EXISTS(SELECT * FROM [dbo].[ExtractLoadManifest] WHERE SystemCode = @SystemCode AND SourceSchema = @Schema AND SourceTableName = @Table))
BEGIN
	RETURN 
END;

WITH [Systems] AS
(
	SELECT 
	LEFT([SourceID], 2) [Order], [SystemCode], MAX([SourceID]) [LastSourceID]
	FROM [dbo].[ExtractLoadManifest] 
	GROUP BY SystemCode, LEFT([SourceID], 2)
)
,[Config] AS
(
	SELECT [RawPath], [TrustedPath], [SourceKeyVaultSecret], [Enabled] 
	FROM   
	( 
		SELECT [Key], [Value] FROM [dbo].[Config]
		WHERE [KeyGroup] = 'IngestionDefault'
	) T
	PIVOT(
		MAX([Value]) 
		FOR [Key] IN (
			[RawPath], 
			[TrustedPath], 
			[SourceKeyVaultSecret],
			[Enabled] 
		)
	) T
)
INSERT INTO [dbo].[ExtractLoadManifest]
([SourceID]
,[SystemCode]
,[SourceSchema]
,[SourceTableName]
,[SourceQuery]
,[SourceKeyVaultSecret]
,[SourceHandler]
,[LoadType]
,[BusinessKeyColumn]
,[WatermarkColumn]
,[RawPath]
,[RawHandler]
,[TrustedHandler]
,[TrustedPath]
,[DestinationSchema]
,[DestinationTableName]
,[ExtendedProperties]
,[Enabled]
,[CreatedDTS])
SELECT 
CASE 
WHEN NOT(EXISTS(SELECT * FROM [Systems])) THEN 20001 /* EMPTY */
WHEN S.[Order] IS NULL THEN CONCAT((SELECT MAX([Order]) FROM [Systems])+1, '001') /*INCREMENT NEW SYSTEM*/
ELSE S.[LastSourceID]+1 /*INCREMENT NEW SOURCE*/
END [SourceID]
,R.[SystemCode]
,[SourceSchema]
,[SourceTableName]
,[SourceQuery]
,[SourceKeyVaultSecret]
,[SourceHandler]
,[LoadType]
,[BusinessKeyColumn]
,[WatermarkColumn]
,[RawPath]
,[RawHandler]
,[TrustedHandler]
,[TrustedPath]
,[DestinationSchema]
,[DestinationTableName]
,[ExtendedProperties]
,[Enabled]
,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time')
FROM (
	SELECT 
	@SystemCode [SystemCode]
	,@Schema [SourceSchema]
	,@Table [SourceTableName]
	,@Query [SourceQuery]
	,COALESCE(@KeyVaultSecret, (SELECT [SourceKeyVaultSecret] FROM [Config])) [SourceKeyVaultSecret]
	,ISNULL(@SourceHandler, 'sql-load') [SourceHandler]
	,NULL [LoadType]
	,NULL [BusinessKeyColumn]
	,@WatermarkColumn [WatermarkColumn]
	,REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
	(SELECT [RawPath] FROM [Config])
	,'$SYSTEM$', @SystemCode) 
	,'$SCHEMA$', @Schema) 
	,'$TABLE$', @Table) 
	,'$EXT$', ISNULL(@RawFileExtension, 'parquet'))
	,'$guid$.', IIF(@RawFileExtension='', '', '$guid$.'))
	[RawPath]
	,'raw-load' [RawHandler]
	,'trusted-load' [TrustedHandler]
	,REPLACE(REPLACE(REPLACE(
	(SELECT [TrustedPath] FROM [Config])
	,'$SYSTEM$', @SystemCode) 
	,'$SCHEMA$', @Schema) 
	,'$TABLE$', @Table)[TrustedPath]
	,REPLACE(REPLACE(@Schema
	,'\', '')
	,' ', '') [DestinationSchema]
	,REPLACE(REPLACE(@Table
	,'\', '')
	,' ', '')[DestinationTableName]
	,@ExtendedProperties [ExtendedProperties]
	,(SELECT [Enabled] FROM [Config]) [Enabled]
) R
LEFT JOIN [Systems] S ON S.[SystemCode] = R.[SystemCode]

END
GO