import requests
from AbstractBeer import Cerveza
from AbstractBeer import AbstractBeer
import sys
from time import sleep

class ApiBeer(AbstractBeer):
    def DatosBeer(self, url):

        REQ = requests.get(url)
        if(REQ.status_code == 200):
            date = REQ.json()

        id = 0
        name = ''
        descripcion = ''
        image = ''
        abv = 0
        ibu = 0
        ebc = 0
        food_pairing = ''
        first_brewed = ''
        ph = 0
        attenuation_level = 0

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

if __name__ == "__main__":
    pagina = ApiBeer()
#    while IDS <= 1:
#        datos = pagina.DatosBeer('https://api.punkapi.com/v2/beers/' +str(IDS) )
#        print(datos)
#        print("\n")
#        sleep(1)
#        IDS += 1
