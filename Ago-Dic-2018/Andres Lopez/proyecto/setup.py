from BDall import *
from TacoScrapi import *
from MetodosBD import *
from MenApi import *
def main():
    urlPedido='http://taco-randomizer.herokuapp.com/'
    urlUsers='https://randomuser.me/api/'
    t=AppTaco()
    u=AppUser()
    db=basedatos()
    for i in range(1, 51):
        taquitos=AppTaco.get_taco(t,urlPedido)
        tq=basedatos.insertarTaco_db(db,i,taquitos)
    for i in range(1, 26):
        usuarios=AppUser.get_usuario(u,urlUsers)
        gg=basedatos.insertarCliente_db(db,i,usuarios)

if __name__ == '__main__':
    main()
