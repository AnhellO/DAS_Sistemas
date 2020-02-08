from bases import *
from taco_scrapi import *
from baseladvd import *
from usuarios_api import *
def main():
    urltacos='http://taco-randomizer.herokuapp.com/'
    urlUsers='https://randomuser.me/api/'
    t=AppTaco()
    u=AppUser()
    db=basedatos()
    for i in range(1, 51):
        taquitos=AppTaco.get_taco(t,urltacos)
        tq=basedatos.insertarTaco_db(db,i,taquitos)
    for i in range(1, 26):
        usuarios=AppUser.get_usuario(u,urlUsers)
        gg=basedatos.insertarCliente_db(db,i,usuarios)

if __name__ == '__main__':
    main()
