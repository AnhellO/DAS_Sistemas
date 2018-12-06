import requests
from bs4 import BeautifulSoup
from AbstractClassBuilders import *
import sys
from time import sleep
#Autor y programador - "Maximiliano García De Santiago"
class ApiCliente(AbstractCliente):
    def DatosCliente(self, url, Id):

        reques = requests.get(url)
        if(reques.status_code == 200):
            DatosUser = reques.json()

        results = DatosUser['results']

        for i in results:
            Genero = i['gender'] #Dato a usar
            Name = i['name']
            Email = i['email'] # Dato a usar
            Dob = i['dob']

        First = Name['first'] #Dato a usar
        Last = Name['last'] #Dato a usar
        Edad = Dob['age'] #Dato a usar
        Nombre = First + ' ' + Last

#        print('----------------------Objeto Creado Cliente----------------')
        return Cliente(Id, Nombre, Genero, Email, Edad)

if __name__ == '__main__':
    UrlCliente = ApiCliente()
#    Id = 0
#    while Id <= 5:
#        datos = UrlCliente.DatosCliente('https://randomuser.me/api/', Id)
#        sleep(1)
#        print(datos)
#        Id += 1
