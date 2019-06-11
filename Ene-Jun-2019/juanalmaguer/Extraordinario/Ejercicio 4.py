
import peewee
import sqlite3

file = 'countries.db'

db = peewee.SqliteDatabase(file)

class Pais(peewee.Model):
    nombre = peewee.TextField()
    lenguajes = peewee.TextField()
    continente = peewee.TextField()
    capital = peewee.TextField()
    zona = peewee.TextField()

    class Meta:
        database = db
        db_table = 'Country'


def count_paises():
    db.connect()
    total = Pais.select().count()
    db.close()
    return total

def data_countries(pais = 'Mexico'):
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    datos = cursor.execute('select * from Paises where Nombre = "{}"'.format(pais)).fetchall()
    conexion.close()
    return datos[0]


def latinos():
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    paises = cursor.execute('select Nombre, Lenguajes from Paises').fetchall()
    hispanohablantes = []
    for pais in paises:
        lenguajes = pais[1].split(',')
        if type(lenguajes) != 'NoneType':
            if 'spa' in lenguajes:
                hispanohablantes.append(pais[0])
    return hispanohablantes

def europeos():
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    paises = cursor.execute('select Nombre from Paises where Continente = "Europe"').fetchall()
    conexion.close()
    return paises


def main():
    print('Total de países: {}'.format(count_paises()))
    print('\nDatos de México: {}'.format(data_countries()))
    paises = latinos()
    print('\nPaíses hispanohablantes: ')
    for pais in paises:
        print(pais)
    paises_europeos = europeos()
    print('\nPaíses de Europa: ')
    for pais in paises_europeos:
        print(pais[0])

if __name__ == '__main__':
    main()