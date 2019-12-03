import BDMusic

def VisualizarTodoArtistas():
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Artist;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nArea: {}\nScore: {}\nComienzo: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()




def VisualizarUnArtista(nombre):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM Artist where artista='{}';".format(nombre)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nArea: {}\nScore: {}\nComienzo: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()





def VisualizarTodoDiscosArtista(artista):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM Discos where artista='{}';"
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nPais: {}\nFecha: {}\nEstado: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()




def ContarTodosArtistas():
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Artist;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

       
        
    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()





def TotalDiscosArtista(artista):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM Discos where artista='{}';".format(artista)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()




def VisualizarPorTag(tags):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM Artist where tag='{}';".format(tags)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nArea: {}\nScore: {}\nComienzo: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()




def VisualizarDiscoPorArtista(id,artista):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM Discos where id='{}' and Artista='{}' ;".format(id,artista)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nArea: {}\nScore: {}\nComienzo: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()







