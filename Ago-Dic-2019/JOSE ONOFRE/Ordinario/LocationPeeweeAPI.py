import requests
import pprint
import ramapi
from ramapi import *
import ClaseLocation
import BDCharacter
import PeeweeLocation
#r = requests.get('https://rickandmortyapi.com/api/character/')

ramapi.Base.api_info()
ramapi.Base.schema()

## Consumir los datos para mandarlos a Peewee

locochon = ramapi.Location.get_all()
#pprint.pprint(locochon)
for n in range(1,5):
    r = requests.get('https://rickandmortyapi.com/api/location/?page={}'.format(n))
    #pprint.pprint(r.json())
    cosa = r.json()
    for location in cosa['results']:

        item = ClaseLocation.Locacion(id = location['id'],name = location['name'],ttype = location['type'],dimension = location['dimension'], residents = location['residents'], url = location['url'], created = location['created'])
        print("-------------Inicio de Locacion--------------\n")
        #print(item)
        PeeweeLocation.InsertarLocation(item)
        print("-------------Final de Locacion--------------\n")

PeeweeLocation.MostrarLocation() #Metodo para mostrar todas las locaciones dentro de la BD creada por Peewee
