create database breakingbad;
use breakingbad;

CREATE TABLE characters (
    char_id int primary key,
    char_name varchar(30),
    char_bd varchar(10),
    char_oc varchar(50),
    char_img varchar(150),
    char_status varchar(20),
    char_nickname varchar(20),
    char_appearance varchar(15),
    char_portrayed varchar(30),
    char_category varchar(50),
    char_bcs_a varchar(15)
);