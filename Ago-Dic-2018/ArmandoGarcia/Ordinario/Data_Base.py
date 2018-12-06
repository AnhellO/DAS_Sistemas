import sqlite3
from abstractDB import *

class Taqueria_db(Abstract_Base_la_dvd):
    def __init__(self):
        self.conn=sqlite3.connect("Taqueria.db")
        self.cursor = self.conn.cursor()

    def insert_Taco_db(self,id_taco,Taquito):
        taco = (id_taco,Taquito.nombre,Taquito.relleno,Taquito.salsas,Taquito.condimentos,Taquito.sasonadores,Taquito.cubierta)
        self.cursor.execute(''' INSERT INTO Taquitos VALUES (?,?,?,?,?,?,?)''',taco)
        self.conn.commit()
        return True

    def insert_User_db(self,id_cliente,Users):
        ap = (id_cliente,Users.name,Users.email,Users.phone,Users.picture,Users.location)
        self.cursor.execute(''' INSERT INTO Users VALUES (?,?,?,?,?,?)''',ap)
        self.conn.commit()
        return True

    def insert_Orden_db(self,id_orden,total,fecha,tipo,id_taco,id_user):
        o = (id_orden,total,fecha,tipo,id_taco,id_user)
        self.cursor.execute(''' INSERT INTO Orden VALUES (?,?,?,?,?,?)''',o)
        self.conn.commit()
        print ('Datos Insertados: ID_orden: {}\nTotal: {}\nFecha: {}\nTipo: {}\nTaco: {}\nCliente: {})'.format(id_orden,total,fecha,tipo,id_taco,id_user))
        return True

    def delete_Orden(self,id_orden):
        self.cursor.execute("DELETE FROM Orden WHERE id_orden = ?",(id_orden,))
        self.conn.commit()
        return True

    def select_Taquitos(self):
        self.cursor.execute("SELECT id_taco,nombre FROM Taquitos group by nombre order by id_taco")
        datos = self.cursor.fetchall()
        if datos:
            return(datos)
        else:
            return('Ya cerramos')

    def select_Orden(self,id_orden):
        odn = id_orden
        self.cursor.execute("SELECT * FROM Orden WHERE id_orden = ?",(odn,))
        datos = self.cursor.fetchone()
        if datos:
            return('ID_orden: {} \nTotal: {} \nFecha: {} \nTipo: {} \nTaco: {} \nCliente: {}'.\
            format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
        else:
            return('La Orden: {} ,no existe'.format(odn))

    def select_User(self):
            self.cursor.execute("SELECT id_user,name,phone from Users")
            datos = self.cursor.fetchall()
            if datos:
                return datos
            else:
                return ("error en la matrix")
                return ("upss error en la matrix")
    def select_user_id(self,id_cliente):
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
