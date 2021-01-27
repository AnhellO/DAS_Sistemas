import sqlite3

conexion = sqlite3.connect('ageofempires.db')

cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS civilization(
    id integer PRIMARY KEY,
    name text,
    expansion text,
    army_type text,
    team_bonus text);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS structure(
    id integer PRIMARY KEY,
    name text,
    description text,
    expansion text,
    age text,
    cost integer);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS technology(
    id integer PRIMARY KEY,
    name text,
    description text,
    expansion text,
    age text,
    cost text);""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS units(
    id integer PRIMARY KEY,
    name text,
    description text,
    expansion text,
    age text);""")