import requests
from BaseDatosTacos import *
import json

class AppCliente(AbstractCliente):
    def get_cliente(self,url):
        request = requests.get(url)
        listadeclientes = request.json()
        name=listadeclientes['results'][0]['name']['first']
        email=listadeclientes['results'][0]['email']
        location=listadeclientes['results'][0]['location']['street']
        phone=listadeclientes['results'][0]['phone']
        picture=listadeclientes['results'][0]['picture']['medium']
        return Cliente(name,email,location,phone,picture)

if __name__ == '__main__':
    app=AppCliente()
    urs = app.get_cliente('https://randomuser.me/api/')
    print(urs.name)
