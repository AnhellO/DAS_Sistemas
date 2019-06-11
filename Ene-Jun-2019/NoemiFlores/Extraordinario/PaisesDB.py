import sqlite3
from Ejercicio3 import Paises

class DataBase():

    def __init__(self, file):
        self.connection = sqlite3.connect(file)

    def CreateTable(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
            cursor.execute("""CREATE TABLE IF NOT EXISTS paises (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      numericCode int,
                                      name text,
                                      nativeName text,
                                      capital text,
                                      region text,
                                      subregion text,
                                      languages text,
                                      )""")

            return ("LA TABLA paises SE CREÓ EXITOSAMENTE")

        except sqlite3.OperationalError:
            return ("OCURRIÓ UN ERROR")

        self.connection.commit()


    def savePaises(self,data):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos
        cursor.execute('''SELECT numericCode FROM paises WHERE numericCode = "{}"'''.format(data.id))

        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'NUMERICCODE':data.id,
            'NAME': data.name,
            'NATIVENAME': data.nativeName,
            'CAPITAL': data.capital,
            'REGION':data.region,
            'SUBREGION':data.subregion,
            'LANGUAGES': data.languages,
            }
            try:
                cursor.execute( "INSERT INTO paises (id, numericCode, name, nativeName, capital, region, subregion, languages) VALUES(null,:NUMERICCODE,:NAME,:NATIVENAME,:CAPITAL,:REGION,:SUBREGION, :LANGUAGES);", parametros)
                self.connection.commit()
                return("EL PAIS: {} SE INSERTÓ EXITOSAMENTE A LA TABLA paises".format(data.name))
            except:
                return("ERROR AL INSERTAR EL PAIS A LA BASE DE DATOS")
            self.connection.commit()
            cursor.execute("""SELECT * FROM paises WHERE numericCode = :NUMERICCODE """, {'NUMERICCODE': character.id})
            consulta = cursor.fetchall()
            list_paises = []
            for p in consulta:
                paises = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
                list_paises.append(paises)
            return list_paises
            self.connection.commit()

        else:
            return "EL PAIS {} YA EXISTE EN LA TABLA paises".format(data.name)

    def showPaises(self):
            # Se hace la conexión a la base de datos
            cursor = self.connection.cursor()
            list = []

            # Se hace la consulta para ver si hay registros
            cursor.execute("""SELECT * FROM paises""")
            registros = cursor.fetchall()
            if registros == []:
                return "NO HAY REGISTROS EN LA TABLA paises"
            else:
                for e in registros:
                    element = (e[1], e[2], e[3], e[4], e[5], e[6], e[7])
                    list.append(element)
                return list


if __name__ == '__main__':
    db = DataBase('paises.db')
    print(db.CreateTable())
    pass