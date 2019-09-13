from bs4 import BeautifulSoup
import requests
from BaseDatosTacos import *

class AppTaco(AbstractTaco):
    def get_taco(self,url):
        req  = requests.get(url)
        data = req.text
        bsoup = BeautifulSoup(data,'lxml')

        nombresoup = bsoup.find('h1')
        nombre = nombresoup.text.strip()
        i = 0

        for recipe in bsoup.find_all('div','recipe'):
            if (i == 0):

                ingrediente = recipe.text.strip()
                ingprincipal = ingrediente

            elif (i == 1):
                ingrediente = recipe.text.strip()
                salsas = ingrediente

            elif (i == 2):
                ingrediente = recipe.text.strip()
                condimentos = ingrediente

            elif (i == 3):
                ingrediente = recipe.text.strip()
                seasonings = ingrediente

            elif (i == 4):
                ingrediente = recipe.text.strip()
                cubierta = ingrediente

            i += 1
        return Taco(nombre,ingprincipal,salsas,condimentos,seasonings,cubierta)
