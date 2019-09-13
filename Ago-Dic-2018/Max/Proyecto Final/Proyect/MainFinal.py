from AbstractClassBuilders import *
from ApiClientes import *
from ScrapiReceta import *
from SqlCrudApi import *
from SqlCrudScrapi import *
from Pedidos import *
from time import sleep
#Autor y programador - "Maximiliano García De Santiago"
def MainProyectTacos():
    crud1 = SqlCRUDReceta()
    crud2 = SqlCRUDCliente()
    crud3 = SqlCRUDPedidos()
    UrlReceta = ScrapTaco()
    UrlCliente = ApiCliente()
    pdd = PedidoVenta()
    ##No me alcanzo tiempo para agregar try catch en caso de IDs no guardadas
    while True: ##Solo funciona con ID guardados, recomiendo primero consulrar el objeto a elegir con una id para despues borrarlo
        opcion = int(input('''Bienvenido al sistema de menu.
       Que accion desea realizar dando un numero:
       1.-Guardar una Receta nueva
       2.-Guardar un Cliente nuevo
       3.-Guardar un Pedido nuevo
       4.-Consultar una Receta Completa
       5.-Consultar un Cliente
       6.-Consultar un Pedido
       7.-Mostrar Lista de Nombres de Recetas
       8.-Mostrar Lista de Clientes
       9.-Mostrar Lista de Pedidos
       10.-Eliminar una Receta de la DB
       11.-Eliminar un Cliente de la DB
       12.-Eliminar un Pedido de la DB
       0.-Salir del menu \n'''))

        if opcion == 0: #Salir del programa main
            print("Que tenga un exelente dia (°w°)/....bye bye")
            break

        elif opcion == 1:
            Id = input('Deme un Id > a 50, que dese dar a la Receta:    ') #Dado que los primero 50 ya estan ocupados
            receta1 = UrlReceta.DatosReceta('http://taco-randomizer.herokuapp.com/', Id)
            newReceta = crud1.CrearReceta(receta1)
            print("Se ha guardado la Receta con exito (°w°)/")
            sleep(1)
            print('\n')
            continue

        elif opcion == 2:
            Id = input('Deme un Id > a 20, que dese dar al Cliente: ') #Dado que los primeros 20 ya estan ocupados
            cliente1 = UrlCliente.DatosCliente('https://randomuser.me/api/', Id)
            newcliente = crud2.CrearCliente(cliente1)
            print("Se ha guardado el Cliente con exito (°w°)/")
            sleep(1)
            print('\n')
            continue

        elif opcion == 3:
            IdPedido = input('Deme un Id > a 5, que dese dar al Pedido: ') # Dado que los primeros 5 ya estan ocupados
            IdReceta = input('Deme un Id de alguna Receta:  ')
            IdCliente = input('Deme un Id de algun Cliente: ')
            pedido = pdd.DatosPedido(IdPedido, IdReceta, IdCliente)
            newPedido = crud3.CrearPedido(pedido)
            print("Se ha guardado el Pedido con exito (°w°)/")
            sleep(1)
            print('\n')
            continue

        elif opcion == 4:
            Id = input('Deme un Id de la Receta que desea consultar:    ')
            ConsultarReceta = crud1.ConsultarReceta(Id)
            sleep(1)
            print('\n')
            continue

        elif opcion == 5:
            Id = input('Deme un Id del Cliente que desea consultar:    ')
            ConsultarCliente = crud2.ConsultarCliente(Id)
            sleep(1)
            print('\n')
            continue

        elif opcion == 6:
            IdPedido = input('Deme un Id del Pedido que desea consultar:    ')
            ConsultarPedido = crud3.ConsultarPedido(IdPedido)
            sleep(1)
            print('\n')
            continue

        elif opcion == 7:
            print('-------------------Esta es la lista de Nombres de Recetas---------------------------')
            MostrarLista = crud1.MostrarListaNombres()
            sleep(1)
            print('\n')
            continue

        elif opcion == 8:
            print('-------------------Esta es la lista de Clientess---------------------------')
            MostrarLista = crud2.MostrarListaClientes()
            sleep(1)
            print('\n')
            continue

        elif opcion == 9:
            print('-------------------Esta es la lista de Pedidos---------------------------')
            MostrarLista = crud3.MostrarListaPedidos()
            sleep(1)
            print('\n')
            continue

        elif opcion == 10:
            Id = input('Deme un Id de la Receta que desea Borrar:    ')
            Borrar = crud1.BorrarReceta(Id)
            print("La Receta a sido Borrada (°w°)/")
            sleep(1)
            print('\n')
            continue

        elif opcion == 11:
            Id = input('Deme un Id del Cliente que desea Borrar:    ')
            Borrar = crud2.BorrarCliente(Id)
            print("El Cliente a sido Borrado (°w°)/")
            sleep(1)
            print('\n')
            continue

        elif opcion == 12:
            Id = input('Deme un Id del Pedido que desea Borrar:    ')
            BorrarPedido = crud3.BorrarPedido(1)
            print("El Pedido a sido Borrado (°w°)/")
            sleep(1)
            print('\n')
            continue

if __name__ == '__main__':
	MainProyectTacos()
