USE [TestData]
GO

/****** Object:  Table [dbo].[students_history]    Script Date: 4/22/2020 1:03:40 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[students_history](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[action] [varchar](20) NOT NULL,
	[student_id] [int] NOT NULL,
	[name] [varchar](20) NOT NULL,
	[age] [int] NOT NULL,
	[address] [char](25) NULL,
	[college] [varchar](100) NULL,
	[updated] [datetime] NULL,
	[updatedby] [varchar](100) NULL,
	[hostname] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

