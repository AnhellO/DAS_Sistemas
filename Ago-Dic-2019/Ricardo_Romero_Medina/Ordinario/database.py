import sqlite3

class basedatos():
    def __init__(self):
        self.crear_tabla_personajes()
        self.crear_tabla_locaciones()
        self.crear_tabla_Episodios()

        

    def crear_tabla_personajes(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = '''
            CREATE TABLE IF NOT EXISTS personajes(
                Id TEXT PRIMARY KEY,
                Nombre TEXT,
                Status TEXT,
                Species TEXT,
                Type TEXT,
                Origin TEXT,
                Location TEXT,
                id_locacion TEXT,
                Episode TEXT,
                id_episodio TEXT,
                Url TEXT,
                foreign key (id_locacion) references locaciones(Id),
                foreign key (id_episodio) references episodios(Id)
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

    def insertar_personajes(self,per):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = """INSERT INTO personajes VALUES 
                    ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(per._Id, per._Nombre, per._Status, per._Species, per._Origen, per._Tipo, per._Location, per._Id_Locacion, per._Episode, per._Id_Episodio, per._Url)
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

    def ver_personajes(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM personajes;'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print('Id: {}\nNombre: {}\nStatus: {}\nSpecies: {}\nOrigen: {}\nTipo: {}\nLocacion: {}\nNumero Locacion: {}\nEpisodio: {}\nNumero Episodio: {}\nURL: {}'.format(*row))
                return 'Id: {}\nNombre: {}\nStatus: {}\nSpecies: {}\nOrigen: {}\nTipo: {}\nLocacion: {}\nNumero Locacion: {}\nEpisodio: {}\nNumero Episodio: {}\nURL: {}'.format(*row)
            print('Total de registros: ', len(rows))
            
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)
            

        finally:
            if(conexion):
                conexion.close()
                print('Conexion a SQLite cerrada\n')

    def crear_tabla_locaciones(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = '''
            CREATE TABLE IF NOT EXISTS locaciones(
                Id TEXT PRIMARY KEY,
                Nombre TEXT,
                Type TEXT,
                Dimension TEXT,
                Residents TEXT,
                id_personaje TEXT,
                Url TEXT, 
                foreign key (id_personaje) references personajes (Id)
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

    def insertar_locaciones(self,loc):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = """INSERT INTO locaciones VALUES 
                    ("{}","{}","{}","{}","{}","{}","{}")""".format(loc._Id, loc._Nombre, loc._Tipo, loc._Dimension, loc._Residentes, loc._Id_Residente, loc._Url)
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
    
    def ver_locaciones(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM locaciones;'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print('Id: {}\nNombre: {}\nTipo: {}\nDimension: {}\nResidente: {}\nNumero Residente: {}\nURL: {}'.format(*row))

            print('Total de registros: ', len(rows))
            
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)
            

        finally:
            if(conexion):
                conexion.close()
                print('Conexion a SQLite cerrada\n')

    def crear_tabla_Episodios(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado a SQLite')

            query = '''
            CREATE TABLE IF NOT EXISTS episodios(
                Id TEXT PRIMARY KEY,
                Nombre TEXT,
                air_date TEXT,
                Episode TEXT,
                Character TEXT,
                id_personaje TEXT,
                Url TEXT, 
                foreign key (id_personaje) references personajes (Id)
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

    def insertar_episodios(self,epi):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = """INSERT INTO episodios VALUES 
                    ("{}","{}","{}","{}","{}","{}","{}")""".format(epi._Id, epi._Nombre, epi._Al_Aire, epi._Episodio, epi._Personaje, epi._Id_Personaje, epi._Url)
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

    def ver_episodios(self):
        try:
            conexion = sqlite3.connect('Ordinario/BaseDatos/rickandmorty.db')
            cursor = conexion.cursor()
            print('Conectado')

            query = 'SELECT * FROM episodios;'
            cursor.execute(query)
            rows = cursor.fetchall()
            print('Total de registros: ', len(rows))

            print('------------Registros-------------')

            for row in rows:
                print('Id: {}\nNombre: {}\nPrimera Transmision: {}\nEpisodio: {}\nPersonaje: {}\nNumero Personaje: {}\nURL: {}'.format(*row))

            print('Total de registros: ', len(rows))
            
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion',error)
            

        finally:
            if(conexion):
                conexion.close()
                print('Conexion a SQLite cerrada\n')

if __name__ == '__main__':
    db = basedatos()
    #db.ver_personajes()
    #db.ver_locaciones()
    #db.ver_episodios()