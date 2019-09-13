import sqlite3

class bd():
    def CrearTablas():
        cnx = sqlite3.connect('taqueria.db')
        cursor = cnx.cursor()

        if cursor.execute('''
            CREATE TABLE IF NOT EXISTS tacos (
            ID integer PRIMARY KEY,
            Nombre_Taco text,
            BaseLayer text,
            Contribuidores_BL text,
            Tags_BL text,
            Mixin text,
            Contribuidores_Mix text,
            Tags_Mix text,
            Condiment text,
            Contribuidores_Cond text,
            Tags_Cond text,
            Seasoning text,
            Contribuidores_Seas text,
            Tags_Seas text,
            Shell text,
            Contribuidores_Shell text,
            Tags_Shell text
            )'''
        ):
            print("Se creó la Tabla tacos")
        else:
            print("Error! No se creó la tabla")

        if  cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
            ID integer PRIMARY KEY,
            Nombre text,
            Genero text,
            Celular text,
            Direccion text
            )'''):
            print("Se creó la Tabla Clientes")
        else:
            print("Error! No se creó la tabla")

        if  cursor.execute('''
            CREATE TABLE IF NOT EXISTS ordenes (
            ID_Orden integer PRIMARY KEY,
            ID_Taco integer,
            ID_Cliente integer,
            NombreTaco text,
            NombreCliente text,
            FOREIGN KEY (ID_Taco) REFERENCES tacos(ID),
            FOREIGN KEY (ID_Cliente) REFERENCES clientes(ID)
            )'''
        ):
            print("Se creó la Tabla Ordenes")
        else:
            print("Error! No se creó la Tabla Ordenes")

        cnx.commit()
        cnx.close()
