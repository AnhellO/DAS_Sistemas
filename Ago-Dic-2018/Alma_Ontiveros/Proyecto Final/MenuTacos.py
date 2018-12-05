from BaseDatosTacos import *
from BDTacos import BasedeDatos
from random import randrange
import time
from datetime import date

print("BIENVENIDO A TACOS CHECO: PROMOCIONES AQUI")
option= int(input("Ver Menu: 1 \nRealizar Pedido: 2 \nVer Pedido: 3 \nCancelar Pedido: 4 \n"))
cont = 0
db = BasedeDatos()
today=date.today()
while cont == 0:
    if option == 1:
        res = BasedeDatos.selectTaco(db)
        print(res)
    elif option == 2:
        cliente = input("Introducir ID de Cliente:")
        c = BasedeDatos.selectCliente(db,cliente)
        if (c == True):
            pedido = int(input("Introducir ID de Taco a ordenar:"))
            if (pedido <= 50):
                id_orden = randrange(100)
                fecha = str(date(today.year,today.month,today.day))
                res1 = BasedeDatos.insertarBDOrden(db,id_orden,'15',fecha,pedido,cliente)
            elif (pedido > 50):
                print("No hay ese tipo de taco en existencia")
    elif option == 3:
        orden = input("Introducir ID de Pedido:")
        res = BasedeDatos.selectOrden(db,orden)
        print(res)
    elif option == 4:
        orden = input("Introducir ID de Pedido para eliminar:")
        res = BasedeDatos.deleteOrden(db,orden)
        if (res == True):
            print("El pedido a sido eliminado")
        else:
            print("El numero de ID de orden no exite")
    else:
        print("Esa opcion no es valida, introduzca otra opcion\n")
    cont= 1
