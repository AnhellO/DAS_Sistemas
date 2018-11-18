import sqlite3

class DataBase():
    conexion = sqlite3.connect('BeerDB.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE Beer
        (Id int PRIMARY KEY NOT NULL,
        Name text NOT NULL,
        Descripcion text NOT NULL,
        Image text NOT NULL,
        Abv real NOT NULL,
        Ibu real NOT NULL,
        Ebc real NOT NULL,
        Food_pairing blob NOT NULL,
        First_brewed text NOT NULL,
        Ph real NOT NULL,
        Attenuation_level real NOT NULL)''')

    conexion.commit()
    conexion.close()
if __name__ == '__main__':
    DataBase()
