import sqlite3

#Creo la base de datos
try:
    conexion = sqlite3.connect('mibd.db')
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
    conexion = sqlite3.connect('mibd.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY,
                name text,
                username text,
                email text,
                street text,
                suite text,
                city text,
                zipcode text,
                lat text,
                lng text,
                phone text,
                website text,
                nameC text,
                catchPhrase text,
                bc text
            );'''

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

