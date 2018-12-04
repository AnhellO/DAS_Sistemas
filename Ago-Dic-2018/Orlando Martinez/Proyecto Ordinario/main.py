import sqlite3
from time import sleep
from base_de_datos import SQlite


conexion = sqlite3.connect('Taqueria.db')
cursor =conexion.cursor()

def MostrarMenu():
    Menu = SQlite.MostrarMenu()
    return Menu

def MostrarOrdenes():
    Ordenes = SQlite.MostrarOrdenes()
    return Ordenes

def MostrarClientes():
    Clientes = SQlite.MostrarClientes()
    return Clientes

def MostrarSubrecetas(taco):
    Subrecetas = SQlite.MostrarSubrecetas(taco)
    return Subrecetas


class main():
    while True:

        opcion = int(input("---Bienvenido a la taqueria ""Los primos""--- \n1.Ver menú \n2.Ordenar \n3.Ver ordenes \n4.Ver clientes \n5.Ver Subrecetas \n0.Salir\n"))
        if opcion==1:
            a=MostrarMenu()
            for b in a:
                print(b)
        if opcion == 2:
            taco = input("Ingresa el id del taco que quires : ")
            cliente = input("Ingresa tu id : ")
            cursor.execute("INSERT INTO Ordenes(id_taco,id_cliente) VALUES(?,?)",(taco,cliente))
            conexion.commit()
            continue
        if opcion==3:
            a=MostrarOrdenes()
            for b in a:
                print(b)
            continue
        if opcion==4:
            a=MostrarClientes()
            for b in a:
                print(b)
        if opcion==5:
            taco = input("Ingresa el id del taco que quires ver las Subrecetas : ")
            a=MostrarSubrecetas(taco,)
            for b in a:
                print(b)

        elif opcion == 0:
            print("Saliendo del menú...")
            sleep(1)
            break
if __name__ == '__main__':
    main()
