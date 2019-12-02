import sqlite3

#Creo la base de datos
try:
    conexion = sqlite3.connect('baseRyM.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de SQLite: ', rows)
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')

#Creo la tabla de usuarios
try:
    conexion = sqlite3.connect('baseRyM.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS Characters (
                id TEXT,
                name TEXT,
                status TEXT,
                species TEXT,
                tipe TEXT,
                gender TEXT,
                nameOrigin TEXT,
                urlOrigin TEXT,
                nameLocation TEXT,
                urlLocation TEXT,
                image TEXT,
                episodes TEXT,
                url TEXT,
                created TEXT
            );'''

    query2 = '''CREATE TABLE IF NOT EXISTS Location (
                id TEXT,
                name TEXT,
                tipe TEXT,
                dimension TEXT,
                residents TEXT,
                url TEXT,
                created TEXT
            );'''

    query3 = '''CREATE TABLE IF NOT EXISTS Episode (
                id TEXT,
                name TEXT,
                air_date TEXT,
                episode TEXT,
                characters TEXT,
                url TEXT,
                created TEXT
            );'''

    cursor.execute(query3)
    cursor.execute(query2)
    cursor.execute(query)
    conexion.commit()
    print('Tabla creada con éxito')
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')