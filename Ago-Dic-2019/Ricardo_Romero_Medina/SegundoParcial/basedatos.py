import sqlite3

def crear_base_datos():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT sqlite_version();'
        cursor.execute(query)
        row = cursor.fetchall()
        print('Version de SQLite: ', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def crear_tabala_artistas():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
        CREATE TABLE IF NOT EXISTS artistas(
            Id TEXT PRIMARY KEY NOT NULL,
            Banda TEXT NOT NULL,
            Tipo TEXT NOT NULL,
            Tag TEXT NOT NULL,
            Area TEXT NOT NULL
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def crear_tabala_discos():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''
        CREATE TABLE IF NOT EXISTS disco(
            Id TEXT PRIMARY KEY NOT NULL,
            Banda TEXT NOT NULL,
            Titulo TEXT NOT NULL,
            Pais TEXT NOT NULL,
            Status TEXT NOT NULL
            );
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        print('Tabla creada correctamente', row)
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion', error)
    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def agregar_artista(banda):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO artistas VALUES 
                ('{}', '{}', '{}', '{}','{}')""".format(banda._Id, banda._Banda, banda._Tipo, banda._Tag, banda._Area)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def agregar_discos(album):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO disco VALUES 
                ('{}', '{}', '{}', '{}','{}')""".format(album._Id, album._Banda, album._Titulo, album._Pais, album._Status)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
            print('Conexion a SQLite cerrada\n')

def Ver_Todos_Artistas():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nBanda: {}\nTipo: {}\nTag: {}\nArea: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Artista():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT Banda FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        lista=[]
        for row in rows:
            lista.append(row[0])
        
        cursor.close()
        return lista

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Un_Artista(banda):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM artistas WHERE banda = '{}';".format(banda)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        
        for row in rows:
            print('Id: {}\nBanda: {}\nTipo: {}\nTag: {}\nArea: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Discos(banda):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT Titulo FROM disco WHERE banda = '{}';".format(banda)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        
        for row in rows:
            print('Id: {}\nBanda: {}\nTitulo: {}\nPais: {}\nStatus: {}'.format(*row))
        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)     

    finally:
        if(conexion):
            conexion.close()

def Ver_Discos_Id_Banda(banda,titulo,id):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT Titulo FROM disco WHERE banda = '{}' and Titulo = '{}' or Id = '{}';".format(banda,titulo,id)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        
        for row in rows:
            print('Id: {}\nBanda: {}\nTitulo: {}\nPais: {}\nStatus: {}'.format(*row))
        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)     

    finally:
        if(conexion):
            conexion.close()

def Ver_Bandas_Totales():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT Banda FROM artistas;"
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))
        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)     

    finally:
        if(conexion):
            conexion.close()

def Ver_Discos_x_Banda(banda):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT Banda FROM disco WHERE banda = '{}';".format(banda)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))
        
        for row in rows:
            if 'Banda' != row['Banda']:
                print('Banda: {}\nTitulo: {}\n'.format(*row))

        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)     

    finally:
        if(conexion):
            conexion.close()

def Ver_Artistas_x_Tag(tag):
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM artistas WHERE tag = '{}';".format(tag)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        
        for row in rows:
            print('Id: {}\nBanda: {}\nTipo: {}\nTag: {}\nArea: {}'.format(*row))
        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)     

    finally:
        if(conexion):
            conexion.close()

def Ver_Todos_Discos():
    try:
        conexion = sqlite3.connect('parcial2.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM disco;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nBanda: {}\nTitulo: {}\nPais: {}\nStatus: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()