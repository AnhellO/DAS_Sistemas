import sqlite3, random, time

cnx = sqlite3.connect('taqueria.db')
cursor = cnx.cursor()

def queryTacos():
    consultarTacos = cursor.execute("SELECT ID, Nombre_Taco FROM tacos")
    return consultarTacos.fetchall()

def queryClientes():
    consultarClientes = cursor.execute("SELECT ID, Nombre FROM clientes")
    return consultarClientes.fetchall()

def queryOrdenes():
    consultarOrdenes = cursor.execute("SELECT ordenes.ID_Orden,ordenes.ID_Taco,ordenes.ID_Cliente,tacos.Nombre_Taco FROM ordenes INNER JOIN tacos ON ordenes.ID_Taco = tacos.ID")
    return consultarOrdenes.fetchall()

def unCliente(idcliente):
    consultaUncliente = cursor.execute("SELECT * FROM clientes WHERE ID=?",(idcliente,))
    return consultaUncliente.fetchall()

def unTaco(idTaco):
    consultaUntaco = cursor.execute("SELECT * FROM tacos WHERE ID=?",(idtaco,))
    return consultaUntaco.fetchall()

def unaOrden(idorden):
    consultaUnaorden = cursor.execute("SELECT * FROM ordenes WHERE ID=?",(idorden,))
    return consultaUnaorden.fetchall()

cnx.commit()

class Main():
    def menu():
        print ("Simulando una Taqueria \n Escoge: ")
        print ("\t1 - Consultar el menu de Tacos")
        print ("\t2 - Ordenar taco")
        print ("\t3 - Ver todos los Clientes")
        print ("\t4 - Ver todas las Ordenes")
        print ("\t5 - Consultar un cliente especifico")
        print ("\t6 - Consultar un taco especifico")
        print ("\t7 - Consultar una orden especifica")
        print ("\t0 - Salir")

    while True:
        menu()
        opcion = input("Selecciona la opción que desees: ")
        if opcion == "1":
            print("\nTecleaste la opcion 1\n")
            todosTacos = queryTacos()
            for taco in todosTacos:
                print(taco,"\n")
            continue
        if opcion == "2":
            print("\nTecleaste la opcion 2\n")
            idorden = random.randint(0,100)
            orden = input("Teclea el ID del taco que deseas ordenar: ")
            cliente = input("Teclea tu ID para registrar tu orden: ")
            cursor.execute("INSERT INTO ordenes (ID_Orden,ID_Taco,ID_Cliente,) VALUES(?,?,?)",(idorden, idtaco, idcliente))
            cnx.commit()
            continue
        if opcion == "3":
            print("\nTecleaste la opcion 3\n")
            todosclientes = queryClientes()
            for cliente in todosclientes:
                print(cliente,"\n")
            continue
        if opcion == "4":
            print("\nTecleaste la opcion 4\n")
            todasordenes = queryOrdenes()
            for orden in todasordenes:
                print(orden,"\n")
            continue
        if opcion == "5":
            print("\nTecleaste la opcion 5\n")
            uncliente = input("Teclea el ID del cliente que quieres consultar: ")
            mostrar = unCliente(uncliente,)
            print(mostrar,"\n")
            continue
        if opcion == "6":
            print("\nTecleaste la opcion 6\n")
            untaco = input("Teclea el ID del taco que quieres consultar: ")
            mostrar = unTaco(untaco)
            print(mostrar,"\n")
            continue
        if opcion == "7":
            print("\nTecleaste la opcion 7\n")
            unaorden = input("Teclea el ID de la orden que quieres consultar: ")
            mostrar = unaOrden(unaorden)
            print(mostrar,"\n")
            continue
        if opcion == "0":
            print("\nTecleaste la opcion 0, salida del menu\n")
            time.sleep(1)
            break

cnx.close()

if __name__ == '__main__':
    Main()
