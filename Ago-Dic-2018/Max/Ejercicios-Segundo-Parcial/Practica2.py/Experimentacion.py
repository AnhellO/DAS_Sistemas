import requests
from AbstractBeer import Cerveza
import sys
#Experimientacion, llevar a cabo la impresiond e todos los ID

def Experiment1():
    page = 1
    while page <= 3:
        url = 'https://api.punkapi.com/v2/beers?page='+str(page)+'&per_page=80'
        REQ = requests.get(url)
        if(REQ.status_code == 200):
            date = REQ.json()
        id = 0
        for i in date:
            id = i['id']
            print(id)
        page += 1

def Experiment2(): #Guardar los datos en objeto
    url = 'https://api.punkapi.com/v2/beers/1'
    REQ = requests.get(url)
    if(REQ.status_code == 200):
        date = REQ.json()

    for i in date:
        id = i['id']
        name = i['name']
        descripcion = i['description']
        image = i['image_url']
        abv = i['abv']
        ibu = i['ibu']
        ebc = i['ebc']
        food_pairing = i['food_pairing']
        first_brewed = i['first_brewed']
        ph = i['ph']
        attenuation_level = i['attenuation_level']
    return Cerveza(id, name, descripcion, image, abv, ibu, ebc, food_pairing, first_brewed, ph, attenuation_level)

#Experiment1()
