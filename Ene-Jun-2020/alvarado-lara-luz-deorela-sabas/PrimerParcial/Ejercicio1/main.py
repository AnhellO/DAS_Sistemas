from Page import Page
from Website import Website

##PRUEBAS CLASE PAGE 
Pag1 = Page(url= 'https://wikileaks.org/', folder='News', link='https://wikileaks.org/Amazon-Atlas-Press-Release.html', titulo='WikiLeaks - Amazon Atlas', desc='',formato='html' )
Pag2 = Page(url= 'https://cuevana3.io', folder='Series', link='https://cuevana3.io/serie/chernobyl', titulo='Chernobyl', desc='La serie relata lo que aconteció en 1986, en uno de los mayores desastres provocados por el hombre en la historia reciente, así como los sacrificios realizados para salvar al continente de un desastre sin precedentes.',formato='JSON' )

#PRUBEAS CLASE WEBSITE
paginas = [Pag1, Pag2]
site = Website('.net','developers.', paginas)

#PRUEBAS FUNCION SEARCH 
print('--------------')
site.search(Pag2)
