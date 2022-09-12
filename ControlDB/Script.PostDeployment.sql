/* POPULATE DEFAULTS FOR [dbo].[Config] */
DECLARE @SummaryOfChanges TABLE(Change VARCHAR(20));
MERGE INTO [dbo].[Config] AS TGT
USING (
	SELECT *
	,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time') [CreatedDTS]
	FROM (
		SELECT 'IngestionDefault' [KeyGroup], 'RawPath' [Key], '/raw/$SYSTEM$/$SCHEMA$_$TABLE$/$yyyy$/$MM$/$dd$/$HH$$mm$/$guid$.$EXT$' [Value]
		UNION SELECT 'IngestionDefault' [KeyGroup], 'TrustedPath' [Key], '/trusted/$SYSTEM$/$SCHEMA$_$TABLE$/' [Value]
		UNION SELECT 'IngestionDefault' [KeyGroup], 'SourceKeyVaultSecret' [Key], '<FILL-ME-IN>' [Value]
		UNION SELECT 'IngestionDefault' [KeyGroup], 'Enabled' [Key], '1' [Value]
		UNION SELECT 'IngestionSheet' [KeyGroup], 'Index' [Key], '0' [Value]
		UNION SELECT 'IngestionSheet' [KeyGroup], 'Limit' [Key], '0' [Value]
		UNION SELECT 'IngestionSheet' [KeyGroup], 'Path' [Key], '<FILL-ME-IN>' [Value]
	) T
)
AS SRC ([KeyGroup],[Key],[Value],[CreatedDTS]) ON TGT.[KeyGroup] = SRC.[KeyGroup] AND TGT.[Key] = SRC.[Key]
WHEN NOT MATCHED BY TARGET THEN
	INSERT ([KeyGroup],[Key],[Value],[CreatedDTS]) VALUES ([KeyGroup],[Key],[Value],[CreatedDTS])
OUTPUT $action 
	INTO @SummaryOfChanges;
SELECT * FROM @SummaryOfChanges;
 