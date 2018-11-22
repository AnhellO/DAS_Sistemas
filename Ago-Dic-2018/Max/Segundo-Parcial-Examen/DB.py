import sqlite3

class DataBase():
    conexion = sqlite3.connect('IceandFire.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE ICEANDFIRE
        (url int PRIMARY KEY NOT NULL,
        name text NOT NULL,
        grender text NOT NULL,
        culture text NOT NULL,
        born text NOT NULL,
        json text NOT NULL)''')

    conexion.commit()
    conexion.close()
if __name__ == '__main__':
    DataBase()
