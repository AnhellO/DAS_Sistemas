from BDall import *
from MetodosBD import basedatos
from random import randrange
import time
from datetime import date

print("bienvenido a los Tacos de perro : 7 C/U")
option= int(input("Ver Menu: 1 \nHacer Pedido: 2 \nMostrar Pedido: 3 \nCancelar Pedido: 4 \n"))
cont = 0
db = basedatos()
today=date.today()
while cont == 0:
    if option == 1:
        res = basedatos.selectTaco(db)
        print(res)
    elif option == 2:
        usuario = input("Introduzca su id:")
        u = basedatos.selectCliente(db,usuario)
        if (u == True):
            pedido = int(input("¿Qué taco va a querer (Introduzca su id)?"))
            if(pedido <= 100):
                id_orden = randrange(100)
                fecha =str(date(today.year, today.month, today.day))
                tipo = input("¿con salsa o sin salsa primo?")
                res1 = basedatos.insertarOrden_db(db,id_orden,'60',fecha,tipo,pedido,usuario)
            elif(pedido > 100):
                print('Se acabo el guiso')
    elif option == 3:
        orden = input("Introduzca su id de Pedido:")
        res = basedatos.selectOrden(db,orden)
        print(res)
    elif option == 4:
        orden = input("Introduzca el id del Pedido a eliminar:")
        res = basedatos.deleteOrden(db,orden)
        if (res == True):
            print('Pedido Eliminado')
        else:
            print('La orden renuncio (no esta)')
    else:
        print("Cambiale primo, no existe esa opcion.\n")
    cont= 1
