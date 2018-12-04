import sqlite3
from AbstractClassBuilders import *
from time import sleep
import sys
#Autor y programador - "Maximiliano García De Santiago"
class SqlCRUDPedidos(AbstractProyectPedido):

        def __init__(self):
            self.conexion = sqlite3.connect('ProyectTaco.db')
            self.cursor = self.conexion.cursor()

        def CrearPedido(self, Pedido):
            pedido = (Pedido.Id, Pedido.Nombre_Receta, Pedido.Nombre_Cliente)
            self.cursor.execute("INSERT INTO Pedidos (Id, Nombre_Cliente, Nombre_Receta) VALUES (?,?,?)", pedido)
            self.conexion.commit()
            Pedido.Id = self.cursor.lastrowid
            print('Pedido guardado')
            return Pedido

        def ConsultarPedido(self, Id):
            self.cursor.execute("SELECT * from Pedidos where Id = ?", [Id])
            for Pedidos in self.cursor.fetchall():
                pedido = Pedido(Pedidos[0], Pedidos[1], Pedidos[2])
            return print(pedido)

        def BorrarPedido(self, Id):
            self.cursor.execute("DELETE from Pedidos WHERE Id=?", [Id])
            self.conexion.commit()
            print('Pedido borrado')
            return True

        def MostrarListaPedidos(self):
            self.cursor.execute("SELECT * from Pedidos")
            for Pedidos in self.cursor.fetchall():
                pedido = Pedido(Pedidos[1], Pedidos[2], Pedidos[0])
                print(pedido)

        def ConsultarReceta(self, Id):
            self.cursor.execute("SELECT * from Recetas where Id = ?", [Id])
            for Recetas in self.cursor.fetchall():
                taco = RecetaTaco(Recetas[1], Recetas[2], Recetas[3], Recetas[4], Recetas[5], Recetas[6], Recetas[0])
                taconame = taco.Id
            return taconame

        def ConsultarCliente(self, Id):
            self.cursor.execute("SELECT * from Clientes where Id = ?", [Id])
            for Clientes in self.cursor.fetchall():
                clt = Cliente(Clientes[0], Clientes[1], Clientes[2], Clientes[3], Clientes[4])
                clientename = clt.Nombre
            return clientename

class PedidoVenta(AbstractPedido):
    def DatosPedido(self, IdPedido, IdReceta, IdCliente):
        crud3 = SqlCRUDPedidos()
        NombReceta = crud3.ConsultarReceta(IdReceta)
        NombCliente = crud3.ConsultarCliente(IdCliente)
        Nombre_Receta = NombReceta
        Nombre_Cliente = NombCliente
#        print(Nombre_Receta)
#        print(Nombre_Cliente)
    #    print('Pedido echo')

        return Pedido(IdPedido, str(Nombre_Receta), str(Nombre_Cliente))


if __name__ == "__main__":
    crud3 = SqlCRUDPedidos()
#    IdPedido = 5
#    IdReceta = 17
#    IdCliente = 4
#    pdd = PedidoVenta()
#    pedido = pdd.DatosPedido(IdPedido, IdReceta, IdCliente)
#    newPedido = crud.CrearPedido(pedido)

#    MostrarLista = crud.MostrarListaPedidos()
#    print(pedido)
#    ConsultarPedido = crud.ConsultarPedido(IdPedido)
#    BorrarPedido = crud.BorrarPedido(1)
