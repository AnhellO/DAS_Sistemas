CREATE TABLE ceos(
    id serial not null,
    index VARCHAR NOT NULL,
    nombre VARCHAR(70) NOT NULL,
    age VARCHAR,
    picture VARCHAR(1000),
    PRIMARY KEY (id)
);

CREATE TABLE companies(
    id serial not null,
    nombre VARCHAR(100),
    email VARCHAR(1000),
    phone VARCHAR(50),
    about VARCHAR(1000),
    direccion VARCHAR(1000),
    registered VARCHAR(100),
    latitude VARCHAR(100),
    longitude VARCHAR(100),
    PRIMARY KEY (id)
);