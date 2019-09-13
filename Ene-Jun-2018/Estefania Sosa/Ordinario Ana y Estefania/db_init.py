import sqlite3
from peewee import *

def main():
    conexion = sqlite3.connect('LIBRERIA.db')
    cursor = conexion.cursor()

    #crear tabla VIDEO
    cursor.execute('''CREATE TABLE AUTOR
                    (ID_AUTOR integer PRIMARY KEY,
                    NOMBRE TEXT NOT NULL,
                    APELLIDO TEXT  NOT NULL)''')

    #crear tabla CATEGORIA
    cursor.execute('''CREATE TABLE EDITORIAL
                    (ID_EDITORIAL integer PRIMARY KEY,
                    NOMBRE_EDITORIAL TEXT NOT NULL,
                    PAIS TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE LIBRO
                    (ID_LIBRO integer PRIMARY KEY,
                    TITULO TEXT NOT NULL,
                    AUTOR_LIBRO TEXT NOT NULL,
                    EDITORIAL_LIBRO TEXT NOT NULL,
                    FOREIGN KEY (AUTOR_LIBRO) REFERENCES AUTOR (NOMBRE),
                    FOREIGN KEY (EDITORIAL_LIBRO) REFERENCES EDITORIAL (NOMBRE_EDITORIAL))''')

    conexion.close()

if __name__ == "__main__":
    main()
    #cursor.execute("INSERT INTO AUTOR (ID_AUTOR,NOMBRE,APELLIDO) VALUES(1,'YO','SOSA')")
    #print(cursor.execute("SELECT * FROM AUTOR"))


 