CREATE TABLE [dbo].[Log](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[ExtractLoadStatusID] [int] NULL,
	[TransformStatusID] [int] NULL,
	[ActivityType] [nvarchar](100) NULL,
	[Message] [nvarchar](max) NOT NULL,
	[CreatedDTS] [datetime] NOT NULL,
 CONSTRAINT [PK_Log] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
