import sqlite3

def main():

	conexion = SqliteDatabase('Libreria_db.db')
	cursor = conexion.cursor()


#crear tabla Libros
	cursor.execute('''CREATE TABLE Libros
                    (id_libro integer PRIMARY KEY,
                    nombre_libro TEXT NOT NULL,
                    autor_libro TEXT NOT NULL,
                    FOREIGN KEY (autor_libro) REFERENCES Autor (nombre_autor),
                    editorial_libro  TEXT NOT NULL,
                    FOREIGN KEY (editorial_libro) REFERENCES Editorial (editorial))'''

    #crear tabla Autor
 	cursor.execute('''CREATE TABLE Autor
                    (id_autor integer PRIMARY KEY,
                    nombre_autor INTEGER NOT NULL,
                    apellidos_autor TEXT NOT NULL''')

    #crear tabla Editorial
	cursor.execute('''CREATE TABLE Editorial
                    (id_editorial integer PRIMARY KEY,
                    editorial INTEGER NOT NULL,
                    pais_editorial TEXT NOT NULL''')


    conexion.close()

if __name__ == "__main__":
    main()