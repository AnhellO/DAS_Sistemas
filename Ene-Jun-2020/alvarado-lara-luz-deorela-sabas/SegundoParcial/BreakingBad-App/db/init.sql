CREATE DATABASE BreakingBad;

use BreakingBad;

CREATE TABLE characters(
    usr_id INT (20) PRIMARY KEY,
    usr_name CHAR (50) NOT NULL,
    usr_birthday CHAR (50) ,
    usr_occupation CHAR (50),
    usr_img CHAR (50),
    usr_stat CHAR (50),
    usr_nickname CHAR (50),
    usr_portrayed CHAR (50),
    usr_category CHAR (50)
);

