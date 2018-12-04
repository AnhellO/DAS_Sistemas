import sqlite3
from BDall import *

class basedatos(AbstractbasePedido):
    def __init__(self):
        self.conn=sqlite3.connect("DBGT.db")
        self.cursor = self.conn.cursor()

    def insertarTaco_db(self,id_taco,Taco):
        t = (id_taco,Taco.nombre,Taco.capa_base,Taco.salsas,Taco.condimentos,Taco.sasonadores,Taco.capas)
        self.cursor.execute(''' INSERT INTO Pedido VALUES (?,?,?,?,?,?,?)''',t)
        self.conn.commit()
        return True

    def insertarCliente_db(self,id_cliente,cliente):
        c = (id_cliente,cliente.name,cliente.email,cliente.phone,cliente.picture,cliente.location)
        self.cursor.execute(''' INSERT INTO Users VALUES (?,?,?,?,?)''',c)
        self.conn.commit()
        return True

    def insertarOrden_db(self,id_orden,total,fecha,tipo,id_taco,id_user):
        o = (id_orden,total,fecha,tipo,id_taco,id_user)
        self.cursor.execute(''' INSERT INTO Orden VALUES (?,?,?,?,?,?)''',o)
        self.conn.commit()
        print ('Datos Insertados: ID_orden: {}\nTotal: {}\nFecha: {}\nTipo: {}\nTaco: {}\nCliente: {})'.format(id_orden,total,fecha,tipo,id_taco,id_user))
        return True

    def deleteOrden(self,id_orden):
        self.cursor.execute("DELETE FROM Orden WHERE id_orden = ?",(id_orden,))
        self.conn.commit()
        return True

    def selectTaco(self):

            self.cursor.execute("SELECT id_taco,nombre FROM Pedido group by Nombre order by id_taco")
            datos = self.cursor.fetchall()
            if datos:
                return(datos)
            else:
                return('Ya cerramos')

    def selectOrden(self,id_orden):
            odn = id_orden
            self.cursor.execute("SELECT * FROM Orden WHERE id_orden = ?",(odn,))
            datos = self.cursor.fetchone()
            if datos:
                return('ID: {} \nTotal: {} \nFecha: {} \nTipo: {} \nTaco: {} \nCliente: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
            else:
                return('La Orden: {} ,no existe'.format(odn))

    def selectCliente(self,id_cliente):
            clt = id_cliente
            self.cursor.execute("SELECT * FROM Users WHERE id_user = ?",(clt,))
            datos = self.cursor.fetchone()
            if datos:
                print('ID: {} \nNombre: {} \nEmail: {} \nTelefono: {} \nDireccion: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4]))
                return True
            else:
                print('El Cliente: {} ,no existe'.format(clt))
                return False

if __name__ == '__main__':
    db=basedatos()
