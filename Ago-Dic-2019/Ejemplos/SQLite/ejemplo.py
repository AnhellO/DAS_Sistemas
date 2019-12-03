import sqlite3

# Conexión simple

try:
    conexion = sqlite3.connect('mi_basesita_de_datos.db')
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

# Creamos una tabla

try:
    conexion = sqlite3.connect('mi_basesita_de_datos.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                contenido TEXT,
                url TEXT NOT NULL
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


# Operaciones CRUD

## INSERT

try:
    conexion = sqlite3.connect('mi_basesita_de_datos.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT * FROM posts;'
    cursor.execute(query)
    rows = cursor.fetchall()

    query = f'''
            INSERT INTO posts
            VALUES (
                NULL,
                'Prueba {len(rows)}',
                'Contenido de prueba {len(rows)}',
                'www.myblog.com/prueba-{len(rows) * 10}'
            );
            '''
    resultado = cursor.execute(query)
    conexion.commit()

    print('Registro insertado exitosamente:', resultado)
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')

## SELECT

try:
    conexion = sqlite3.connect('mi_basesita_de_datos.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT * FROM posts;'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Total de registros:', len(rows))

    print('##### Registros #####')
    for row in rows:
        print('Id: {}\nTítulo: {}\nContenido: {}\nURL: {}'.format(*row))
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')