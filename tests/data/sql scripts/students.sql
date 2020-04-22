USE [TestData]
GO

/****** Object:  Table [dbo].[students]    Script Date: 4/22/2020 1:03:27 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[students](
	[id] [int] NOT NULL,
	[name] [varchar](20) NOT NULL,
	[age] [int] NOT NULL,
	[address] [char](25) NULL,
	[college] [varchar](100) NULL,
	[updated] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

