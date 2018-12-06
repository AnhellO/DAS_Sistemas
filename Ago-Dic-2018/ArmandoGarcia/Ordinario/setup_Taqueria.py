from abstractTaco import *
from abstractUsuario import *
from abstractDB import *
from Scrapi_taco import *
from Data_Base import *
from API_User import *
class setup_taqueria():
    def setup():
        urltacos='http://taco-randomizer.herokuapp.com/'
        urlUsers='https://randomuser.me/api/'
        t=Taquito_Scrapt()
        u=API_User()
        db=Taqueria_db()
        for i in range(1, 51):
            taquitos=Taquito_Scrapt.get_taquito(t,urltacos)
            tq=Taqueria_db.insert_Taco_db(db,i,taquitos)
        for i in range(1, 26):
            usuarios=API_User.get_user(u,urlUsers)
            gg=Taqueria_db.insert_User_db(db,i,usuarios)

if __name__ == '__main__':
    setup_taqueria.setup()
