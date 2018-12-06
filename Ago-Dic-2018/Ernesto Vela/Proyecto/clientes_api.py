import requests
from abstractas import *
import json
class ClientesApi(ClienteAbstracto):
    def get_cliente(self,url):
        request = requests.get(url)
        lista_clientes = request.json()
        name=lista_clientes['results'][0]['name']['first']
        email=lista_clientes['results'][0]['email']
        phone=lista_clientes['results'][0]['phone']
        picture=lista_clientes['results'][0]['picture']['medium']
        location=lista_clientes['results'][0]['location']['street']
        return Cliente(name, email, phone, picture, location)

if __name__ == '__main__':
    x = ClientesApi()
    cli = x.get_cliente('https://randomuser.me/api/')
    print(cli.name)
