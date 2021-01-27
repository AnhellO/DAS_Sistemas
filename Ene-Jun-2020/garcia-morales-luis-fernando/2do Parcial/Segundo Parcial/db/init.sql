CREATE DATABASE BreakingDb;
USE BreakingDb;

CREATE TABLE personajes (
	id INT(10) NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50),
	fechaNac VARCHAR(10),
    ocupacion VARCHAR(50),
	imagen VARCHAR(350),
    estado VARCHAR(20),
    nickname VARCHAR(20),
    apariciones VARCHAR(15),
    actor VARCHAR (50),
    categoria VARCHAR(20),
	CONSTRAINT id_pk PRIMARY KEY (id)
);