CREATE SERVER DAS_SISTEMAS;
\c DAS_SISTEMAS
CREATE DATABASE dc_heroes;
\c dc_heroes;
CREATE TABLE IF NOT EXISTS SUPER_HEROE(
    id int NOT NULL,
    name varchar(50),
    full_name varchar(200),
    alter_egos varchar(200),
    aliases varchar(200),
    place_of_birth varchar(200),
    first_appearance varchar(200),
    publisher varchar(200),
    alignment varchar(200),
    gender varchar(200),
    race varchar(200),
    height varchar(200),
    weight varchar(200),
    eye_color varchar(200),
    hair_color varchar(200),
    occupation text,
    base text,
    group_affiliation text,
    relatives text,
    image text,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS SUPERHEROES_STATS(
    id VARCHAR(10) ,
    intelligence VARCHAR(10),
    strength VARCHAR(10),
    speed VARCHAR(10),
    durability VARCHAR(10),
    power VARCHAR(10),
    COMBAT VARCHAR(10),
    PRIMARY KEY (id)
);