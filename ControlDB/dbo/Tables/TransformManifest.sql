CREATE TABLE [dbo].[TransformManifest] (
    [TransformID]          INT            NOT NULL,
    [EntityType]           NVARCHAR (50)  NOT NULL,
    [EntityName]           NVARCHAR (100) NOT NULL,
    [ProcessorType]        NVARCHAR (50)  NOT NULL,
    [TargetKeyVaultSecret] NVARCHAR (50)  NOT NULL,
    [Command]              NVARCHAR (200) NOT NULL,
    [Dependancies]         NVARCHAR (50)  NULL,
    [ParallelGroup]        INT            NOT NULL,
    [Enabled]              BIT            NOT NULL,
    [CreatedDTS]           DATETIME       NOT NULL,
    CONSTRAINT [PK_TransformationManifest] PRIMARY KEY CLUSTERED ([TransformID] ASC)
);




GO
