import sqlite3

def main():
    conexion = sqlite3.connect('2p.db')
    cursor = conexion.cursor()

    #crear tabla VIDEOJUEGO
    cursor.execute('''CREATE TABLE JUEGO
                    (ID integer PRIMARY KEY,
                    NOMBRE TEXT NOT NULL,
                    GENERO TEXT NOT NULL,
                    CATEGORIA TEXT NOT NULL)''')

    #crear tabla CONSOLA
    cursor.execute('''CREATE TABLE CONSOLA
                    (ID integer PRIMARY KEY,
                    NOMBRE INTEGER NOT NULL,
                    MARCA TEXT NOT NULL)''')

    conexion.close()

if __name__ == "__main__":
    main()
