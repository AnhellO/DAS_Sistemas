import requests
from bs4 import BeautifulSoup
from AbstractClassBuilders import *
import sys
from time import sleep
#Autor y programador - "Maximiliano García De Santiago"
class ScrapTaco(AbstractReceta):
    def DatosReceta(self, url, Id):
        REQ = requests.get(url)

        BS = BeautifulSoup(REQ.text, 'html.parser')
        div_principal = BS.find_all('div',{'class':'row'})

        Nombre_Receta = BS.find('h1')
        Contribuidores = BS.find_all('h6',{'class':'light'})
        Sub_receta_1 = div_principal[1].find('div',{'class':'recipe'})
        Sub_receta_2 = div_principal[2].find('div',{'class':'recipe'})
        Sub_receta_3 = div_principal[3].find('div',{'class':'recipe'})
        Sub_receta_4 = div_principal[4].find('div',{'class':'recipe'})

#        print('----------------------Objeto Receta Creada-----------------------')
        return RecetaTaco(Id, str(Nombre_Receta), str(Contribuidores), str(Sub_receta_1), str(Sub_receta_2), str(Sub_receta_3), str(Sub_receta_4))

if __name__ == '__main__':
    UrlReceta = ScrapTaco()
#    Id = 0
#    while Id <= 0:
#        datos = UrlReceta.DatosReceta('http://taco-randomizer.herokuapp.com/', Id)
#        sleep(1)
#        print(datos)
#        Id += 1
