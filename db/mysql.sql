DROP TABLE IF EXISTS itunes;
CREATE TABLE itunes (
  guid CHAR(32) PRIMARY KEY,
  name TEXT,
  thumbnail TEXT,
  url TEXT,
  updated DATETIME
) DEFAULT CHARSET=utf8;

