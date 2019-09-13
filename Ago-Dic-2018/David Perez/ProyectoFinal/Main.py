from bases import *
from baseladvd import basedatos
from random import randrange
import time
from datetime import date

print("Bienvenido a los Tacos : El taco a 20")
option= int(input("Ver Menú: 1 \nRealizar Pedido: 2 \nVer Pedido: 3 \nCancelar Pedido: 4 \n"))
cont = 0
db = basedatos()
today=date.today()
while cont == 0:
    if option == 1:
        res = basedatos.selectTaco(db)
        print(res)
    elif option == 2:
        usuario = input("Introduzca su id de Usuario:")
        u = basedatos.selectCliente(db,usuario)
        if (u == True):
            pedido = int(input("¿Qué taco va a ordenar (Introduzca su id)?"))
            if (pedido <= 50):
                id_orden = randrange(100)
                fecha = str(date(today.year,today.month,today.day))
                tipo = input("¿Para comer aquí o para llevar?")
                res1 = basedatos.insertarOrden_db(db,id_orden,'20',fecha,tipo,pedido,usuario)
            elif (pedido > 50):
                print('Ese Taco no existe.')
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
            print('La orden no existe')
    else:
        print("Introduzca una opción válida.\n")
    cont= 1
