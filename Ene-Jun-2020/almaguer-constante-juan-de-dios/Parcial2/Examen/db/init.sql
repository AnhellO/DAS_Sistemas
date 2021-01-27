CREATE DATABASE breaking;
use breaking;

CREATE TABLE IF NOT EXISTS characters (
	id INT(10) NOT NULL,
	name VARCHAR(50),
	birthday VARCHAR(150),
	img VARCHAR(350),
	estado VARCHAR(15),
	nickname VARCHAR(15),
	portrayed VARCHAR(20),
	CONSTRAINT character_pk PRIMARY KEY (id)
);