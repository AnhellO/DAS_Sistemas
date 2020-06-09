create database BreakBad;
use BreakBad;

CREATE TABLE IF NOT EXISTS characters (
    id INT(10) PRIMARY KEY,
    name VARCHAR (50),
    birthday VARCHAR (50),
    occupation VARCHAR (50),
    img VARCHAR (200),
    status VARCHAR (50),
    nickname VARCHAR (50),
    portrayed VARCHAR (50),
    category VARCHAR (50)
    );