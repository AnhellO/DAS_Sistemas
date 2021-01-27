CREATE DATABASE ejercicio_5;
USE ejercicio_5;
CREATE TABLE countries (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    population INT(10),
    name VARCHAR(100) NOT NULL,
    alpha_3_code VARCHAR(10) NOT NULL,
    capital VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    subregion VARCHAR(50) NOT NULL,
    flag VARCHAR(250) NOT NULL
)