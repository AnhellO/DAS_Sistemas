from abstractas import *
from database import takosdb
from random import randrange
import time
from datetime import date
class takazos():
    def chefer():

        print("Los meros takos")
        cont = 0
        db = takosdb()
        today = date.today()
        while True:
            option= int(input("Tacos disponibles: 1 \nOrdenar: 2 \nVer Orden: 3 \nCancelar Orden: 4 \nSalir: 5 \n"))
            if option == 1:
                res = takosdb.select_tako(db)
                print(res)
                print('\n')
            elif option == 2:
                usuario = input("id de Cliente:")
                u = takosdb.select_Cliente(db,usuario)
                if (u == True):
                    pedido = int(input("De cual taco va a ordenar?"))
                    if(pedido <= 100):
                        id_orden = randrange(100)
                        fecha =str(date(today.year, today.month, today.day))
                        tipo = input("De harina o de maiz?")
                        res1 = takosdb.insertar_Orden(db,id_orden,'55',fecha,tipo,pedido,usuario)
                        print('\n')
                    elif(pedido > 100):
                        print('Se acabo ese taco joven')
            elif option == 3:
                orden = input("id de Orden:")
                res = takosdb.select_Orden(db,orden)
                print(res)
                print('\n')
            elif option == 4:
                orden = input("id de orden que desea cancelar:")
                res = takosdb.delete_Orden(db,orden)
                if (res == True):
                    print('Orden cancelada')
                    print('\n')
                else:
                    print('No se encontro esa orden')
                    print('\n')
            elif option == 5:
                break
            else:
                print("Revise las opciones.\n")
            cont= 1

if __name__ == '__main__':
    takazos.chefer()
