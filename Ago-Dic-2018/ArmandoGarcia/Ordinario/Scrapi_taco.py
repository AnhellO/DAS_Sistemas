from bs4 import BeautifulSoup
import requests
from abstractTaco import *
class Taquito_Scrapt(AbstractTaquitos):
    def get_taquito(self,url):
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html5lib')

        name_box = soup.find('h1')
        nombre = name_box.text.strip()
        i = 0
        for recipe in soup.find_all('div','recipe'):
            if (i == 0):
                ingrediente = recipe.text.strip()
                relleno = ingrediente

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
                cubierta = ingrediente

            i += 1

        return Taquito(nombre,relleno,salsas,condimentos,sasonadores,cubierta)
if __name__ == '__main__':
    y=Taquito_Scrapt()
    a = y.get_taquito('http://taco-randomizer.herokuapp.com/')
    print(a.nombre)
