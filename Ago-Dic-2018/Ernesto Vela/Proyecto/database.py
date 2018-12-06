import sqlite3
from abstractas import *

class takosdb(BaseAbstracta):
    def __init__(self):
        self.conn=sqlite3.connect("Tako_db.db")
        self.cursor = self.conn.cursor()

    def insertar_tako(self,id_tako,Tako):
        t = (id_tako,Tako.nombre,Tako.principal,Tako.salsas,Tako.condimentos,Tako.sasonadores,Tako.shell)
        self.cursor.execute(''' INSERT INTO Takos VALUES (?,?,?,?,?,?,?)''',t)
        self.conn.commit()
        return True

    def insertar_Cliente(self,id_cliente,Cliente):
        c = (id_cliente,Cliente.name,Cliente.email,Cliente.phone,Cliente.picture,Cliente.location)
        self.cursor.execute(''' INSERT INTO Clientes VALUES (?,?,?,?,?,?)''',c)
        self.conn.commit()
        return True

    def insertar_Orden(self,id_orden,total,fecha,tipo,id_tako,id_user):
        o = (id_orden,total,fecha,tipo,id_tako,id_user)
        self.cursor.execute(''' INSERT INTO orden VALUES (?,?,?,?,?,?)''',o)
        self.conn.commit()
        print ('id_orden: {}\nTotal: {}\nFecha: {}\nTipo: {}\nTako: {}\nCliente: {})'.format(id_orden,total,fecha,tipo,id_tako,id_user))
        return True

    def delete_Orden(self,id_orden):
        self.cursor.execute("DELETE FROM orden WHERE id_orden = ?",(id_orden,))
        self.conn.commit()
        return True

    def select_tako(self):

            self.cursor.execute("SELECT id_tako,nombre FROM Takos group by Nombre order by id_tako")
            datos = self.cursor.fetchall()
            if datos:
                return(datos)
            else:
                return('Ya cerramos')

    def select_Orden(self,id_orden):
            odn = id_orden
            self.cursor.execute("SELECT * FROM orden WHERE id_orden = ?",(odn,))
            datos = self.cursor.fetchone()
            if datos:
                return('ID: {} \nTotal: {} \nFecha: {} \nTipo: {} \nTako: {} \nCliente: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
            else:
                return('La orden: {} ,no existe'.format(odn))

    def select_Cliente(self,id_cliente):
            cli = id_cliente
            self.cursor.execute("SELECT * FROM Clientes WHERE id_user = ?",(cli,))
            datos = self.cursor.fetchone()
            if datos:
                print('ID: {} \nNombre: {} \nEmail: {} \nTelefono: {} \nPicture: {} \nDireccion: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
                return True
            else:
                print('El Cliente: {} ,no existe'.format(cli))
                return False

if __name__ == '__main__':
    db=basedatos()
