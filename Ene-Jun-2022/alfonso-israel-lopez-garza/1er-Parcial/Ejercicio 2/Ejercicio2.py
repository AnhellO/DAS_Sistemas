from __future__ import annotations
from abc import ABC, abstractmethod
class Director:
    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder:Builder) -> None:
        self._builder = builder
    
    def build_complete(self) ->None:
        self.a = ""
        self.a += str(self.builder.getElement1()) +"\n"
        self.a += str(self.builder.getElement2()) +"\n"
        self.a += str(self.builder.getElement3()) +"\n"
        self.a += str(self.builder.getElement4()) +"\n"
        self.a += str(self.builder.getElement5()) +"\n"
        self.a += str(self.builder.getElement6()) +"\n"
        self.a += str(self.builder.getElement7()) +"\n"
        return self.a

class Builder(ABC):
    @abstractmethod
    def getElement1(self) ->None:
        pass

    @abstractmethod
    def getElement2(self) ->None:
        pass

    @abstractmethod
    def getElement3(self) ->None:
        pass

    @abstractmethod
    def getElement4(self) ->None:
        pass

    @abstractmethod
    def getElement5(self) ->None:
        pass

    @abstractmethod
    def getElement6(self) ->None:
        pass

    @abstractmethod
    def getElement7(self) ->None:
        pass

class PageBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._page = Page()
    
    def setUrl(self,url):
        self._page.url = url
    
    def setFolder(self,folder):
        self._page.folder = folder
    
    def setLink(self,link):
        self._page.links = link
    
    def setParrafo(self,parrafo):
        self._page.parrafo = parrafo
    
    def setTitulo(self,titulo):
        self._page.titulo = titulo
    
    def setFormato(self,formato):
        self._page.formato = formato
    
    def setMetaDescripcion(self,metadescripcion):
        self._page.metaDescripcion = metadescripcion
    
    def getElement1(self):
        return f"Dirección Url: {self._page.url}"
    
    def getElement2(self):
        return f"Folder: {self._page.folder}"

    def getElement3(self):
        return f"link: {self._page.links}"

    def getElement4(self):
        return f"<p> {self._page.parrafo} </p>"
    
    def getElement5(self):
        return f"<h1> {self._page.titulo} </h1>"
    
    def getElement6(self):
        return f"Formato: {self._page.formato}"

    def getElement7(self):
        return f"Meta-Descripción: {self._page.metaDescripcion}"

class WebsiteBuilder(Builder):    
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._website = Website()
    
    def setDominio(self,dominio):
        self._website.dominio = dominio
    
    def setSubdominio(self,subdominio):
        self._website.subdominio = subdominio
    
    def setPaginas(self,paginas: list):
        self._website.paginas = paginas
    
    def setExtension(self,extension):
        self._website.extension = extension
    
    def setDescripcion(self,descripcion):
        self._website.descripcion = descripcion
         
    def setHost(self,host):
        self._website.host = host
    
    def setLenguaje(self,lenguaje):
        self._website.language = lenguaje
         
    def getElement1(self):
        return f"Dominio: {self._website.dominio}"

    def getElement2(self):
        return f"Subdominio: {self._website.subdominio}"

    def getElement3(self):
        self.pagina = "Paginas: \n"
        for pag in self._website.paginas:
            self.pagina += pag
            self.pagina += "\n"
        return self.pagina

    def getElement4(self):
        return f"Extension: {self._website.extension}"

    def getElement5(self):
        return f"Descripcion: {self._website.descripcion}"

    def getElement6(self):
        return f"Host: {self._website.host}"

    def getElement7(self):
        return f"Lenguaje: {self._website.language}"

class Page():
    def __init__(self,url = None,folder = None,link = None,parrafo = None,titulo = None,formato = None,metaDescripcion = None,body = None,image = None) -> None:
        self.url = url
        self.folder =folder
        self.links = link
        self.parrafo =parrafo
        self.titulo =titulo
        self.formato = formato
        self.metaDescripcion = metaDescripcion
        self.body = body
        self.image = image


class Website():
    def __init__(self,dominio = None,subdominio = None ,paginas = None,extension = None,descripcion = None,host = None,language = None) -> None:
        self.dominio = dominio
        self.subdominio = subdominio
        self.paginas = paginas
        self.extension = extension
        self.descripcion = descripcion
        self.host = host
        self.language = language

def main():
    paginas = []
    '''Primera Pagina'''
    director = Director()
    builder = PageBuilder()
    builder.setUrl("www.pagina1.com")
    builder.setFolder("Pagina")
    builder.setLink("Paginitas.com.mx")
    builder.setParrafo("Mi primera pagina")
    builder.setTitulo("Iniciando")
    builder.setFormato("HTML")
    builder.setMetaDescripcion("Creando pagina")
    director._builder = builder
    paginas.append(director.build_complete())

    '''Segunda pagina'''
    director = Director()
    builder = PageBuilder()
    builder.setUrl("www.pagina2.com")
    builder.setFolder("Pagina")
    builder.setLink("Tacos.mx")
    builder.setParrafo("Tacos el esquinaso")
    builder.setTitulo("Ricos tacos")
    builder.setFormato("JSON")
    builder.setMetaDescripcion("Pagina de tacos")
    director._builder = builder
    paginas.append(director.build_complete())

    '''Sitio web'''
    director = Director()
    builder = WebsiteBuilder()
    builder.setDominio("Publico")
    builder.setSubdominio("Mexicano")
    builder.setPaginas(paginas)
    builder.setDescripcion("Random")
    builder.setExtension(".mx")
    builder.setHost("Servidor saltillo 3")
    builder.setLenguaje("Español")
    director._builder = builder

    print("Sitio Web")
    print(director.build_complete())

if __name__ == "__main__":
    main()