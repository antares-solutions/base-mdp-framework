CREATE TABLE [dbo].[ExtractLoadManifest](
	[SourceID] [int] NOT NULL,
	[SystemCode] [nvarchar](50) NOT NULL,
	[SourceSchema] [nvarchar](100) NULL,
	[SourceTableName] [nvarchar](100) NULL,
	[SourceQuery] [nvarchar](max) NULL,
	[SourceFolderPath] [nvarchar](200) NULL,
	[SourceFileName] [nvarchar](100) NULL,
	[SourceKeyVaultSecret] [nvarchar](100) NULL,
	[SourceMetaData] [nvarchar](max) NULL,
	[SourceHandler] [nvarchar](100) NOT NULL,
	[LoadType] [nvarchar](50) NULL,
	[BusinessKeyColumn] [nvarchar](100) NULL,
	[WatermarkColumn] [nvarchar](100) NULL,
	[RawHandler] [nvarchar](max) NULL,
	[RawPath] [nvarchar](max) NULL,
	[TrustedHandler] [nvarchar](max) NULL,
	[TrustedPath] [nvarchar](max) NULL,
	[DestinationSchema] [nvarchar](100) NULL,
	[DestinationTableName] [nvarchar](100) NULL,
	[DestinationKeyVaultSecret] [nvarchar](100) NULL,
	[ExtendedProperties] [nvarchar](max) NULL,
	[Enabled] [bit] NOT NULL,
	[CreatedDTS] [datetime] NOT NULL,
 CONSTRAINT [PK_SourceManifest] PRIMARY KEY CLUSTERED 
(
	[SourceID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
