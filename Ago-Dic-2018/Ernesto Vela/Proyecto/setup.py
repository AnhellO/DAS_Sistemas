from abstractas import *
from tako_scrap import *
from database import *
from clientes_api import *
class setupTakos():
    def main():
        urltacos='http://taco-randomizer.herokuapp.com/'
        urlUsers='https://randomuser.me/api/'
        t = TakoScrap()
        u = ClientesApi()
        db = takosdb()
        for i in range(1, 51):
            takitos = TakoScrap.get_tako(t,urltacos)
            tq = takosdb.insertar_tako(db,i,takitos)
        for i in range(1, 26):
            Clientes = ClientesApi.get_cliente(u,urlUsers)
            gg = takosdb.insertar_Cliente(db,i,Clientes)

if __name__ == '__main__':
    setupTakos.main()
