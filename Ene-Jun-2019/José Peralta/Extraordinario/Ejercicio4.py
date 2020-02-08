import peewee
import sqlite3

file = 'paises.db'
db = peewee.SqliteDatabase(file)

class Pais(peewee.Model):
    nombre = peewee.TextField()
    lenguajes = peewee.TextField()
    continente = peewee.TextField()
    capital = peewee.TextField()
    zona = peewee.TextField()

    class Meta:
        database = db
        db_table = 'Paises'

# Hice una versión anterior de contar_paises(), pero no usaba peewee,
# por lo que la borré.

def contar_paises():
    db.connect()
    total = Pais.select().count()
    db.close()
    return total

def datos_pais(pais = 'Mexico'):
    conexion = sqlite3.connect(file)
    cursor = conexion.cursor()
    datos = cursor.execute('select * from Paises where Nombre = "{}"'.format(pais)).fetchall()
    conexion.close()
    return datos[0]

# Esta estaba planeada como una versión del código anterior que funcionara
# usando peewee, pero no entendía por qué fallaba y decidí seguir adelante.

# def datos_pais(pais = 'Mexico'):
#     db.connect()
#     datos = Pais.select().where(Pais.nombre.in_(pais))
#     db.close()
#     return datos

def hispanohablantes():
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

# El caso de este es igual al de 'datos_pais()'

# def europeos():
#     db.connect()
#     paises = Pais.select(Pais.nombre).where(Pais.continente == 'Europe')
#     db.close()
#     return paises

def main():
    print('Total de países: {}'.format(contar_paises()))
    print('\nDatos de México: {}'.format(datos_pais()))
    paises = hispanohablantes()
    print('\nPaíses hispanohablantes: ')
    for pais in paises:
        print(pais)
    paises_europeos = europeos()
    print('\nPaíses de Europa: ')
    for pais in paises_europeos:
        print(pais[0])

if __name__ == '__main__':
    main()
