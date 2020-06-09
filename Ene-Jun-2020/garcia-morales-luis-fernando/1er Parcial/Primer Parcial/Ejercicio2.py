import abc
from Ejercicio1 import Page
class PageComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ContenidoPagina():
        pass

class TagOpen(PageComponent):
    def ContenidoPagina(self):
        return '<p'

class Estilo(PageComponent):
    def __init__(self, style: PageComponent):
        self.style = style

    def ContenidoPagina(self):
    		return f'{self.style.ContenidoPagina()} style = "color:blue;">'

class TagClose(PageComponent):
    def __init__(self, style: PageComponent):
        self.style = style
        
    def ContenidoPagina(self):
        return f"{self.style.ContenidoPagina()} </p>"
class InsertarContenido(PageComponent):
    def __init__(self, contenido):
        self.contenidoPagina = contenido
    def ContenidoPagina(self):
        return f"{Estilo.ContenidoPagina()}{self.ContenidoPagina}</p>"
class main():
    pagina1 = Page(
        url="mail.google.com",
        path="mail.google.com/mail/u/0/#inbox", 
        contenido="Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        titulo="<h1>Gmail</h1>",
        title="<title>Recibidos</title>",
        metadesc="Correo Electrnico",
        formato="html")

    tagOpen = TagOpen()
    estilo = Estilo(tagOpen)
    print(InsertarContenido(pagina1.get_contenido()))
    