import ordinario
import time
import sqlite3

if __name__ == '__main__':

    tacoapi = ordinario.TacoApi('http://taco-randomizer.herokuapp.com/')
    clientesapi = ordinario.ApiCliente('https://randomuser.me/api/')
    bd = ordinario.Sqlite('BasedeTacos.db')
    bd.crearBD()

    clientes = clientesapi.get_cliente()
    bd.insert_cliente(clientes)

    for i in range(0, 50):
        datos = tacoapi.get_info()
        bd.insert_ingrediente(datos)
        bd.insert_taco(datos)

    print('Clientes registrados')

    persona = bd.get_cliente()
    cantidad = persona.ordenar()
    persona.comer(cantidad)

    persona2 = bd.get_cliente()
    cantidad = persona2.ordenar()
    persona2.comer(cantidad)

    persona3 = bd.get_cliente()
    cantidad = persona3.ordenar()
    persona3.comer(cantidad)
