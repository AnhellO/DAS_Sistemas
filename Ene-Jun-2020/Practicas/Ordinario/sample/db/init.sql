CREATE DATABASE pokedex;
\c pokedex;

CREATE TABLE pokemon (
	id SERIAL NOT NULL,
	nombre VARCHAR(50),
	tipos VARCHAR(150),
	imagen VARCHAR(350),
	PRIMARY KEY (id)
);