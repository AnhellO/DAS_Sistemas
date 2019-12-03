import sqlite3

def Comprobar_Version():
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
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

#Create

def Crear_Tabla():
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                contenido TEXT,
                URL TEXT NOT NULL
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

#Insert
def Agregar_Elemento(Titulo_Nota, Contenido_Nota, Url_Nota):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO posts VALUES 
                (NULL, '{}', '{}', '{}')""".format(Titulo_Nota, Contenido_Nota, Url_Nota)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()



#Select

def Ver_Todo():
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM posts;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nTitulo: {}\nContenido: {}\nURL: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


#Select Simgular

def Ver_Uno(id_elemento):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM posts where Id = {};'.format(id_elemento)
        cursor.execute(query)
        rows = cursor.fetchall()

        print('----------Registro id = {}-------------'.format(id_elemento))

        for row in rows:
            print('Id: {}\nTitulo: {}\nContenido: {}\nURL: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


#Delete

def Eliminar_Elemento(Id_Elemento):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "DELETE FROM posts WHERE id = {}".format(Id_Elemento)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Eliminado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


#Update

def Actualizar_Elemento(id_elemento, espacio, nuevo_valor):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """UPDATE posts SET {} = '{}' where Id = {}""".format(espacio, nuevo_valor, id_elemento)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Actualizado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
