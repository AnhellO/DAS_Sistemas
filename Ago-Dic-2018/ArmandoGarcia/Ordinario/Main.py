from abstractDB import *
from Data_Base import *
from random import randrange
import time
from datetime import date
class principal():
    def Taqueria():
        print("Bienvenido a los Taco Madre : La Orden a $60 wuera pasele pasele")
        gg = 0
        db = Taqueria_db()
        today=date.today()
        while True:
            a= int(input("Menu de Taquitos: 1 \nRealizar Pedido: 2 \nMostrar Pedido: 3 \nCancelar Pedido: 4 \nLista de Clientes: 5 \nSalir: 6 \n"))
            if a == 1:
                results = Taqueria_db.select_Taquitos(db)
                print(results)
                print("\n")
            elif a == 2:
                usuario = input("Introduzca su id de Usuario:")
                u = Taqueria_db.select_user_id(db,usuario)
                if (u == True):
                    pedido = int(input("¿Que taquito desea ordenar (Introduzca su id)?"))
                    if(pedido <= 50):
                        id_orden = randrange(100)
                        fecha =str(date(today.year, today.month, today.day))
                        tipo = input("¿Con queso o sin queso?")
                        res1 = Taqueria_db.insert_Orden_db(db,id_orden,'60',fecha,tipo,pedido,usuario)
                        print("\n")
                    elif(pedido > 50):
                        print('De ese no tenemos')

            elif a == 3:
                orden = input("Introduzca su id de Pedido:")
                results = Taqueria_db.select_Orden(db,orden)
                print(results)
                print("\n")

            elif a == 4:
                orden = input("Introduzca el id del Pedido a eliminar:")
                results = Taqueria_db.delete_Orden(db,orden)
                if (results == True):
                    print('Orden Eliminado')
                    print("\n")
                else:
                    print('La orden no existe')
            elif a == 5:
                results = Taqueria_db.select_User(db)
                print(results)
                print("\n")
            elif a == 6:
                break
            else:
                print("Introduzca una opción válida.\n")
if __name__ == '__main__':
    principal.Taqueria()
