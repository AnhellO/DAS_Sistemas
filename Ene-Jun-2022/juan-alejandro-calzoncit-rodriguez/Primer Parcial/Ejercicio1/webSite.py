from page import *

'''
Clase WebSite que representa a un sitio web
'''

class WebSite:
    def __init__(self, dominio=None,subdominio=None,extension = None,paginas=None,descripcion=None,hosting=None,adaptadoMoviles = False) -> None:
            # Atributos
            self.dominio = dominio
            self.subdominio = subdominio
            self.extension = extension
            self.paginas = paginas  # Es una lista de objetos de tipo Page
            self.descripcion = descripcion
            self.hosting = hosting
            self.adaptadoMoviles = adaptadoMoviles
    
    # Setters
    def setDominio(self,dominio):
        self.dominio = dominio

    def setSubdominio(self,subdominio):
        self.subdominio = subdominio

    def setExtension(self,extension):
        self.extension = extension

    def setPaginas(self,paginas):
        self.paginas = paginas

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setHosting(self,hosting):
        self.hosting = hosting

    def setAdaptadoMoviles(self,adaptadoMoviles):
        self.adaptadoMoviles = adaptadoMoviles


    # Función la cúal busca un objeto Page dentro del atributo paginas
    def buscador(self,pag : Page, web = None ):
        if web != None:
            if pag in web.paginas:
                return('Encontrado')
        if pag in self.paginas:
            return('Encontrado')
        return('No encontrado')