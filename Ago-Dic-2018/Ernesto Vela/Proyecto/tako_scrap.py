from bs4 import BeautifulSoup
import requests
from abstractas import *
class TakoScrap(TakoAbstracto):
    def get_tako(self,url):
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html5lib')

        name_box = soup.find('h1')
        nombre = name_box.text.strip()
        i = 0
        for recipe in soup.find_all('div','recipe'):
            if (i == 0):
                ingrediente = recipe.text.strip()
                capa_base = ingrediente
            elif (i == 1):
                ingrediente = recipe.text.strip()
                salsas = ingrediente
            elif (i == 2):
                ingrediente = recipe.text.strip()
                condimentos = ingrediente
            elif (i == 3):
                ingrediente = recipe.text.strip()
                sasonadores = ingrediente
            elif (i == 4):
                ingrediente = recipe.text.strip()
                capas = ingrediente
            i += 1

        return Tako(nombre,capa_base,salsas,condimentos,sasonadores,capas)
if __name__ == '__main__':
    y=TakoScrap()
    takaso = y.get_tako('http://taco-randomizer.herokuapp.com/')
    print(takaso.nombre)
