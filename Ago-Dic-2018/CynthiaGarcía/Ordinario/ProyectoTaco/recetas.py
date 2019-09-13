from bs4 import BeautifulSoup
import requests
import re
from tacoCRUD import Crud


#para la extracción de datos con BeautifulSoup es necesario instalar un lector, en este caso se utilizo "lxml"
class Recetas():
    def __init__(self):
        self.url = 'http://taco-randomizer.herokuapp.com'
        self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml') 

    def getTaco(self):
        self.nombreTaco = self.soup.find('h1', class_='light').text.strip() #se busca en titulo "light"
        self.recipes = []
        recetas = self.soup.findAll('div', class_='recipe') #se crea una lista de las recetas con la etiqueta('recipe') para acceder a los indices del elemento "light"
        for receta in recetas:
            self.recipes.append(receta.text.strip())
        return self

    
"""
r = Recetas()
o = r.getTaco()

# print(o.recipes)

# for r in o.recipes:
#     print(r.text.strip())

c = Crud()
s=RecetaBD()
t=TacoBD()
print(o.nombreTaco)
c.agregaTaco(o.nombreTaco)
c.agregaReceta(s.id, t.id, s.nombrereceta)
"""