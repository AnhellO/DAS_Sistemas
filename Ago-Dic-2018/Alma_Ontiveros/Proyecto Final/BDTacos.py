import sqlite3
from BaseDatosTacos import *

class BasedeDatos (AbstractBDTacos):
    def __init__(self):
        self.conn=sqlite3.connect("BDTacos.db")
        self.cursor = self.conn.cursor()

    def insertarBDCliente (self,id_cliente,Cliente):
        clientes = (id_cliente,Cliente.name,Cliente.email,Cliente.location,Cliente.phone,Cliente.picture)
        self.cursor.execute(''' INSERT INTO CLIENTE VALUES (?,?,?,?,?,?)''', clientes)
        self.conn.commit()
        return True

    def insertarBDTacos (self,id_taco,Taco):
        taquito = (id_taco,Taco.name,Taco.ingprincipal,Taco.salsas,Taco.condimentos,Taco.seasonings,Taco.cubierta)
        self.cursor.execute(''' INSERT INTO TACOS VALUES (?,?,?,?,?,?,?)''', taquito)
        self.conn.commit()
        return True

    def insertarBDOrden (self,id_orden,total,fecha,id_taco,id_cliente):
        ordenar = (id_orden,total,fecha,id_taco,id_cliente)
        self.cursor.execute(''' INSERT INTO ORDEN VALUES (?,?,?,?,?)''', ordenar)
        self.conn.commit()
        print ('ID: {}\nTotal: {}\nFecha: {}\nTaco: {}\nCliente: {}'.format(id_orden,total,fecha,id_taco,id_cliente))
        return True

    def deleteOrden(self,id_orden):
        self.cursor.execute("DELETE FROM ORDEN WHERE id_orden = ?",(id_orden,))
        self.conn.commit()
        return True

    def selectTaco(self):
            self.cursor.execute("SELECT id_taco,name FROM TACOS group by name order by id_taco")
            datos = self.cursor.fetchall()
            if datos:
                return(datos)
            else:
                return("No exiten tacos.")

    def selectOrden(self,id_orden):
            ordens = id_orden
            self.cursor.execute("SELECT * FROM ORDEN WHERE id_orden = ?",(ordens,))
            datos = self.cursor.fetchone()
            if datos:
                return('ID: {} \nTotal: {} \nFecha: {} \nTaco: {} \nCliente: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4]))
            else:
                return('La Orden: {}, no existe'.format(ordens))

    def selectCliente(self,id_cliente):
            client = id_cliente
            self.cursor.execute("SELECT * FROM CLIENTE WHERE id_cliente = ?",(client,))
            datos = self.cursor.fetchone()
            if datos:
                print('ID: {} \nNombre: {} \nEmail: {} \nFoto: {} \nTelefono: {} \nDireccion: {}'.\
                format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
                return True
            else:
                print('El Cliente: {}, no existe'.format(client))
                return False

if __name__ == '__main__':
    db=BasedeDatos()
