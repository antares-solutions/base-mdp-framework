CREATE TABLE [dbo].[ReportRefreshStatus](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BatchID] [nvarchar](16) NULL,
	[ReportName] [nvarchar](100) NOT NULL,
	[SourceTable] [nvarchar](100) NOT NULL,
	[Status] [nvarchar](100) NOT NULL,
	[CreatedDTS] [datetime] NOT NULL,
	[StartDTS] [datetime] NOT NULL,
	[EndDTS] [datetime] NOT NULL,
 CONSTRAINT [PK_ReportRefreshStatus] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO