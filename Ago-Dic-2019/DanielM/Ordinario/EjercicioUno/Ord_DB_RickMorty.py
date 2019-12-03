import sqlite3

# Crear BD
try:
    conexion = sqlite3.connect('Ord_DB_RickMorty.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de SQLite: ', rows)
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión crack :(', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')







#Crear Tabla Personajes
try:
    conexion = sqlite3.connect('Ord_DB_RickMorty.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    pers = '''CREATE TABLE IF NOT EXISTS Characters (
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

    loc = '''CREATE TABLE IF NOT EXISTS Location (
                id TEXT,
                name TEXT,
                tipe TEXT,
                dimension TEXT,
                residents TEXT,
                url TEXT,
                created TEXT
            );'''

    epi = '''CREATE TABLE IF NOT EXISTS Episode (
                id TEXT,
                name TEXT,
                air_date TEXT,
                episode TEXT,
                characters TEXT,
                url TEXT,
                created TEXT
            );'''

    cursor.execute(epi)
    cursor.execute(loc)
    cursor.execute(pers)
    conexion.commit()
    print('Tabla creada :v')
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión crack :(', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')