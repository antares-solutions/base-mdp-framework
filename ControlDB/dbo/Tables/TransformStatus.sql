CREATE TABLE [dbo].[TransformStatus](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BatchID] [varchar](64) NOT NULL,
	[TransformID] [int] NOT NULL,
	[SpotCount] [bigint] NULL,
	[InsertCount] [bigint] NULL,
	[UpdateCount] [bigint] NULL,
	[CuratedCount] [bigint] NULL,
	[Status] [nvarchar](50) NULL,
	[StartDTS] [datetime] NULL,
	[EndDTS] [datetime] NULL,
	[CreatedDTS] [datetime] NOT NULL,
 CONSTRAINT [PK_TransformStatus_1] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
