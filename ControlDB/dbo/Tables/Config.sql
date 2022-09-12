CREATE TABLE [dbo].[Config] (
    [KeyGroup]   NVARCHAR (200) NOT NULL,
    [Key]        NVARCHAR (200) NOT NULL,
    [Value]      NVARCHAR (200) NULL,
    [CreatedDTS] DATETIME       NOT NULL,
    CONSTRAINT [PK_Config] PRIMARY KEY CLUSTERED ([KeyGroup] ASC, [Key] ASC)
);



