import peewee
import sqlite3

file = 'Paises.db'
db = peewee.SqliteDatabase(file)

class Pais(peewee.Model):
    name = peewee.TextField()
    capital = peewee.TextField()
    region = peewee.TextField()
    languages = peewee.TextField()
    flag = peewee.TextField()

    class Meta:
        database = db
        db_table = 'Paises'

def contar_paises():
    db.connect()
    total = Pais.select().count()
    db.close()
    return total

def datos_pais(pais = 'Mexico'):
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    datos = cursor.execute('SELECT * FROM Paises WHERE Nombre = "{}"'.format(pais)).fetchall()
    conexion.close()
    return datos[0]

def hispanos():
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    paises = cursor.execute('SELECT Nombre, Lenguajes FROM Paises').fetchall()
    hispanohablantes = []
    for pais in paises:
        languages = pais[1].split(',')
        if type(languages) != 'NoneType':
            if 'spa' in languages:
                hispanohablantes.append(pais[0])
    return hispanohablantes

def europa():
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    paises = cursor.execute('SELECT Nombre FROM Paises WHERE Region = "Europe"').fetchall()
    conexion.close()
    return paises

def main():
    print('-Total de Paises: {}'.format(contar_paises()))
    print('\n-Datos de México: {}'.format(datos_pais()))
    paises = hispanos()
    print('\n---Paises Hispanohablantes---')
    for pais in paises:
        print('\t*' + pais)
    paises_europeos = europa()
    print('\n---Paises de Europa---')
    for pais in paises_europeos:
        print('\t*' + pais[0])

if __name__ == '__main__':
    main()
