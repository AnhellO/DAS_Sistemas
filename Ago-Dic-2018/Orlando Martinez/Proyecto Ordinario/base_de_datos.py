import sqlite3


class SQlite():
    def MostrarMenu():
            conexion = sqlite3.connect('Taqueria.db')
            cursor =conexion.cursor()
            MostrarMenu=cursor.execute("SELECT ID_TACO, NOMBRE_TACO FROM Tacos")
            return MostrarMenu.fetchall()

    def MostrarOrdenes():
          conexion = sqlite3.connect('Taqueria.db')
          cursor =conexion.cursor()
          MostrarOrdenes=cursor.execute("SELECT Ordenes.id_orden,Ordenes.id_cliente,Ordenes.id_taco,Tacos.NOMBRE_TACO FROM Ordenes INNER JOIN Tacos ON Ordenes.id_taco=Tacos.ID_TACO")
          return MostrarOrdenes.fetchall()

    def MostrarClientes():
          conexion = sqlite3.connect('Taqueria.db')
          cursor =conexion.cursor()
          MostrarClientes=cursor.execute("SELECT Ordenes.id_orden,Clientes.ID_CLIENTE,Clientes.NOMBRE_CLIENTE,Clientes.DIRECCION,Clientes.CELULAR FROM Ordenes INNER JOIN Clientes ON Ordenes.id_cliente=Clientes.ID_CLIENTE")
          return MostrarClientes.fetchall()

    def MostrarSubrecetas(taco):
            conexion = sqlite3.connect('Taqueria.db')
            cursor =conexion.cursor()
            MostrarMenu=cursor.execute("SELECT SUBRECETAS FROM Tacos WHERE ID_TACO=?",(taco,))
            return MostrarMenu.fetchall()

    def Close(self):
        self.conexion.close()




if __name__ == '__main__':
    base_de_datos.Close()
