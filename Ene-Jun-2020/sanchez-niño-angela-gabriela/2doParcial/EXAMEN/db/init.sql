CREATE DATABASE personajes;
use personajes;

CREATE TABLE personaje (
	id INT(10) NOT NULL AUTO_INCREMENT,
	names VARCHAR(50),
	birthday VARCHAR(150),
	occupation VARCHAR(150),
	imagen VARCHAR(350),
    status1 VARCHAR (150),

	CONSTRAINT personaje_pk PRIMARY KEY (id)
);