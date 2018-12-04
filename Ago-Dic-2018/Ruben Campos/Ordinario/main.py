import ordi
import time
import sqlite3

if __name__ == '__main__':
    apiclientes = ordi.ClientsApi('https://randomuser.me/api/')
    tacoapi = ordi.TacoApi('http://taco-randomizer.herokuapp.com/')
    sqlite = ordi.Sqlite('primera-prueba.db')
    sqlite.createDB()

    # clientes = apiclientes.get_clients()
    # sqlite.insert_cliente(clientes)
    # for i in range(0, 50):
    #     info = tacoapi.get_info()
    #     sqlite.insert_ingrediente(info)
    #     sqlite.insert_taco(info)
    #     print('Registrado')

    for i in range(0,10):
        persona = sqlite.get_cliente()
        cant = persona.ordenar_taquito()
        print('\nEspere sus taquitos...\n')
        time.sleep(2)
        persona.comer(cant)

    db = sqlite3.connect('primera-prueba.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM Orden WHERE Cantidad > 8''')
    masdeocho = len(cursor.fetchall())
    print('Se han vendido en total {} ordenes de mas de 8 tacos!'.format(masdeocho))

    cursor.execute('''SELECT * FROM Orden WHERE Total > 150''')
    venta = len(cursor.fetchall())
    print('Se han hecho {} ventas con ganancias de 150 pesos o mas!'.format(venta))
