


CREATE PROCEDURE [dbo].[LogMessage] 
	@ID INT = NULL,
	@IsTransform BIT = 0,
	@ActivityType VARCHAR(100) = NULL,
	@Message VARCHAR(MAX)
AS
BEGIN
	IF @IsTransform = 1
	BEGIN
		INSERT INTO [dbo].[Log] 
		([TransformStatusID]
		,[ActivityType]
		,[Message]
		,[CreatedDTS]) 
		SELECT @ID
		,@ActivityType
		,@Message
		,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time')
	END
	ELSE
	BEGIN
		INSERT INTO [dbo].[Log] 
		([ExtractLoadStatusID]
		,[ActivityType]
		,[Message]
		,[CreatedDTS]) 
		SELECT @ID
		,@ActivityType
		,@Message
		,CONVERT(DATETIME, CONVERT(DATETIMEOFFSET, GETDATE()) AT TIME ZONE 'AUS Eastern Standard Time')
	END
END
GO