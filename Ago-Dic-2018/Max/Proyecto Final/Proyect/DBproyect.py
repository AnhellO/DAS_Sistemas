import sqlite3
#Autor y programador - "Maximiliano García De Santiago"
class DataBase():
    conexion = sqlite3.connect('ProyectTaco.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE Recetas
                    (Id int PRYMARY KEY NOT NULL,
                    Nombre_Receta text NOT NULL,
                    Contribuidores text,
                    Sub_receta_1 text,
                    Sub_receta_2 text,
                    Sub_receta_3 text,
                    Sub_receta_4 text)''')

    cursor.execute('''CREATE TABLE Clientes
                    (Id int PRYMARY KEY NOT NULL,
                    Nombre text NOT NULL,
                    Genero text,
                    Email text,
                    Edad text)''')

    cursor.execute('''CREATE TABLE Pedidos
                    (Id int PRYMARY KEY NOT NULL,
                    Nombre_Cliente text NOT NULL,
                    Nombre_Receta text NOT NULL)''')

if __name__ == '__main__':
    DataBase()
