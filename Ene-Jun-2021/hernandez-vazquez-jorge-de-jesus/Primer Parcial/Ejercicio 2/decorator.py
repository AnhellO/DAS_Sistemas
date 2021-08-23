import abc

class PaginaWeb(object):

    # Constructor
    def __init__(self, url, ruta, formato,
                 contenido, titulo, slug, metatags: list):

        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.metatags = metatags

        # Funcion __str__ para obtener una vista de
        # La pagina web y sus atributos

    def __str__(self):

        return f"""\nURL: {self.url}\nRUTA: {self.ruta}\nFORMATO: {self.formato}\nCONTENIDO: {self.contenido}\nTITULO: {self.titulo}\nSLUG: {self.slug}\nMETA-TAGS: {self.metatags}"""

    #Clase componente del sitio web que 
    #Establece la interfaz para los objetos
class SitioWebComponent(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def searching(self) -> str:
        pass

    #Clase componente concreto del sitio web
    #Que define el comportamiento del decorador
class SitiowebConcreteComponent(SitioWebComponent,metaclass=abc.ABCMeta ):
    
    def __init__(self, dominio, categoria, paginas: PaginaWeb):

        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas

    def __str__(self) -> str:
        return f"""\nDOMINIO: {self.dominio}\nCATEGORIA: {self.categoria}\nPAGINAS: {self.paginas}"""


    def searching(self):
        return "ERROR 404, page not found"

    #Clase decoradora base del sitio web, que implementa
    # Un campo de tipo interfaz (SitioWebComponent), para que
    # Pueda contener a los componentes concretos, asi como a los
    # Decoradores       
class SitioWebBaseDecorator(SitioWebComponent, metaclass=abc.ABCMeta):

    def __init__(self, SitioWeb: SitioWebComponent):
        self.SitioWeb = SitioWeb 

    @abc.abstractmethod
    def searching(self) -> str:
        pass

    #La clase decorador concreto del sitio web define 
    #Funcionanlidades adicionales que se añaden a los 
    #Componentes
class SearchingConcreteDecorator(SitioWebBaseDecorator):
    
    #Decorador 
    def searching(self, pag: PaginaWeb):
        cont=0
        for pag in self.SitioWeb.paginas:
            if pag.url == self.SitioWeb. paginas[cont].url: #.url
                return f"LA PÁGINA:\n{self.SitioWeb.paginas[cont]}\n\nSI EXISTE :D"
        return "ERROR 404, page not found"

    #Funcion main donde agregaremos objetos a nuestras clases
def main():

    # Declaramos una variable de tipo "PaginaWeb" para
    # añadirle datos a los atributos de la clase de la pagina web.
    pag1 = PaginaWeb(url="www.georgeUadec.com", ruta="/root",
                     formato="HTML", contenido="<body> ¡¡This is Sparta!! </body> ",
                     titulo="<title> Live long and Prosper </title>", slug="Live-long-and-Prosper",
                     metatags=["<meta name="">", "<meta http-equiv="">", "<meta content="" ", "<meta charset=UTF-8>"])

    # Imprimimos para ver la informacion del sitio web y la pagina
    #print(pag1)

    pag2 = PaginaWeb(url="www.github.com", ruta="/root/repo",
                     formato="HTML", contenido="<header> ¡¡DAS_Sistemas!! </header> ",
                     titulo="<title> Repositorio DAS </title>", slug="Repositorio-DAS",
                     metatags=["<meta name="">", "<meta content="" "])


    # Lo mismo para la clase del Sitio web.
    sitio1 = SitiowebConcreteComponent(dominio="georgeuadec.com", categoria="Blog",
                      paginas=[pag1, pag2])

    #s = PaginaWeb(url="www.youtube.com", ruta="/profile",
    #                 formato="HTML", contenido="<li> Musica </li> ",
    #                 titulo="<title> ¡¡YouTube Mx!! </title>", slug="YouTube-Mx",
    #                 metatags=["<meta name="">", "<meta content="" "])

    s1 = SitiowebConcreteComponent("georgeuadec.com", "Blog", [pag1, pag2])
    search = SearchingConcreteDecorator(s1)
    search2 = search.searching(pag1)
    print(search2)

if __name__ == "__main__":
    # Funcion main que contiene nuestros objetos de clase
    main()
