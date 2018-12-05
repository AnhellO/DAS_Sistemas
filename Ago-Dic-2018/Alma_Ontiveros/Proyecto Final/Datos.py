from BaseDatosTacos import *
from AppTaco import *
from BDTacos import *
from AppCliente import *

def main():
    urltacos='http://taco-randomizer.herokuapp.com/'
    urlcliente='https://randomuser.me/api/'
    taco=AppTaco()
    cliente=AppCliente()
    db=BasedeDatos()

    for i in range(1, 51):
        tacos=AppTaco.get_taco(taco,urltacos)
        dbtaco=BasedeDatos.insertarBDTacos(db,i,tacos)
    for i in range(1, 51):
        clientes=AppCliente.get_cliente(cliente,urlcliente)
        dbcliente=BasedeDatos.insertarBDCliente(db,i,clientes)

if __name__ == '__main__':
    main()
