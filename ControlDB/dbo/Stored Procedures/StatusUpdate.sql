CREATE PROCEDURE [dbo].[StatusUpdate] 
	@TableName VARCHAR(50),
	@ID INT,
	@Property VARCHAR(MAX),
	@Value VARCHAR(MAX)
AS
BEGIN

	DECLARE @IDProperty VARCHAR(50) = IIF(@TableName IS NULL, 'SourceID', 'TransformID')
	SET @TableName = COALESCE(@TableName, 'ExtractLoadStatus')

	DECLARE @SQL NVARCHAR(4000) = 
	REPLACE(REPLACE(REPLACE(REPLACE(
	'UPDATE [dbo].[$TableName$] 
	SET [$Property$] = ''$Value$''
	WHERE [ID] = ''$ID$'''
	,'$TableName$', @TableName)
	,'$Property$', @Property)
	,'$Value$', @Value)
	,'$ID$', @ID)
	EXECUTE ( @SQL )
	
END
GO
