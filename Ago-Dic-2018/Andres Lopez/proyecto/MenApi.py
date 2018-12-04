import requests
from BDall import *
import json
class AppUser(AbstracClient):
    def get_usuario(self,url):
        request = requests.get(url)
        lista_clientes = request.json()
        name=lista_clientes['results'][0]['name']['first']
        email=lista_clientes['results'][0]['email']
        phone=lista_clientes['results'][0]['phone']
        picture=lista_clientes['results'][0]['picture']['medium']
        location=lista_clientes['results'][0]['location']['street']
        return cliente(name,email,phone,picture,location)

if __name__ == '__main__':
    x=AppUser()
    urs = x.get_usuario('https://randomuser.me/api/')
    print(urs.name)
