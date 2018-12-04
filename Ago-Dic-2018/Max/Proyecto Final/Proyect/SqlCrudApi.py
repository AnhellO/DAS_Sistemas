import sqlite3
from ApiClientes import *
from AbstractClassBuilders import *
import sys
#Autor y programador - "Maximiliano García De Santiago"
class SqlCRUDCliente(AbstractProyectClient):

    def __init__(self):
        self.conexion = sqlite3.connect('ProyectTaco.db')
        self.cursor = self.conexion.cursor()

    def CrearCliente(self, Cliente):
        cliente = (Cliente.Id, Cliente.Nombre, Cliente.Genero, Cliente.Email, Cliente.Edad)
        self.cursor.execute("INSERT INTO Clientes (Id, Nombre, Genero, Email, Edad) VALUES (?,?,?,?,?)", cliente)
        self.conexion.commit()
        Cliente.Id = self.cursor.lastrowid
        print('cliente guardado')
        return Cliente

    def MostrarListaClientes(self):
        self.cursor.execute("SELECT * from Clientes")
        for Clientes in self.cursor.fetchall():
            clt = Cliente(Clientes[1], Clientes[2], Clientes[3], Clientes[4], Clientes[0])
            print(clt)

    def ConsultarCliente(self, Id):
        self.cursor.execute("SELECT * from Clientes where Id = ?", [Id])
        for Clientes in self.cursor.fetchall():
            clt = Cliente(Clientes[0], Clientes[1], Clientes[2], Clientes[3], Clientes[4])
        return print(clt)

    def BorrarCliente(self, Id):
        self.cursor.execute("DELETE from Clientes WHERE Id=?", [Id])
        self.conexion.commit()
        print('Cliente borrado')
        return True


if __name__ == "__main__":
    UrlCliente = ApiCliente()
    crud2 = SqlCRUDCliente()
#    Id = 6
#    Borrar = crud.BorrarCliente(5)
#    MostrarLista = crud.MostrarListaClientes()
#    ConsultarCliente = crud.ConsultarCliente(Id)
#    while Id <= 20:
#        cliente1 = UrlCliente.DatosCliente('https://randomuser.me/api/', Id)
#        newcliente = crud.CrearCliente(cliente1)
#        sleep(1)
#        Id += 1
