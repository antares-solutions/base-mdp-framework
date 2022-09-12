CREATE TABLE [dbo].[ExtractLoadStatus](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BatchID] [varchar](64) NOT NULL,
	[SystemCode] [nvarchar](100) NOT NULL,
	[SourceID] [int] NOT NULL,
	[LowWatermark] [nvarchar](100) NULL,
	[HighWatermark] [nvarchar](100) NULL,
	[SourceRowCount] [bigint] NULL,
	[SinkRowCount] [bigint] NULL,
	[RawPath] [nvarchar](200) NULL,
	[RawStatus] [nvarchar](50) NULL,
	[RawStartDTS] [datetime] NULL,
	[RawEndDTS] [datetime] NULL,
	[TrustedStatus] [nvarchar](50) NULL,
	[TrustedStartDTS] [datetime] NULL,
	[TrustedEndDTS] [datetime] NULL,
	[CreatedDTS] [datetime] NOT NULL,
	[EndedDTS] [datetime] NULL,
 CONSTRAINT [PK_ExtractLoadStatus] PRIMARY KEY CLUSTERED 
(
	[ID] ASC,
	[BatchID] ASC,
	[SystemCode] ASC,
	[SourceID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO