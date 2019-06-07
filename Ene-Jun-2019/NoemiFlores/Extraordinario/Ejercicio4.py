import peewee
import sqlite3

file = 'paises.db'

db = peewee.SqliteDatabase(file)

class Pais(peewee.Model):
    numericCode = peewee.TextField()
    name = peewee.TextField()
    nativeName = peewee.TextField()
    capital = peewee.TextField()
    region = peewee.TextField()
    subregion = peewee.TextField()
    languages = peewee.TextField()

    class Meta:
        database = db
        db_table = 'paises'


def count_paises():
    db.connect()
    total = Pais.select().count()
    db.close()
    return total

def data_countries(pais = 'Mexico'):
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    datos = cursor.execute('SELECT * FROM paises WHERE name = "{}"'.format(pais)).fetchall()
    connection.close()
    return datos[0]


def spanish():
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    paises = cursor.execute('SELECT name, languages FROM paises').fetchall()
    idiomaEspañol = []
    for data in paises:
        lenguajes = data[1].split(',')
        if type(lenguajes) != 'NoneType':
            if 'spa' in lenguajes:
                spanish.append(data[0])
    return idiomaEspañol


def main():
    print('Cantidad total de paises: {}'.format(count_paises()))
    print('\nDatos de México: {}'.format(data_countries()))
    print('\nPaíses con el idioma español:{}'.format(spanish()))
    for pais in spanish():
        print(pais)

if __name__ == '__main__':
    main()