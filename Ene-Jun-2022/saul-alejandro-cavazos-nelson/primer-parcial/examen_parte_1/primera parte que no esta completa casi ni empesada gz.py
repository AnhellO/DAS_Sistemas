from abc import ABC, abstractmethod

class page (ABC):
    @abstractmethod
    def Url(self):
        url=""
    @abstractmethod
    def folder(self):
        archivos=[]
    @abstractmethod
    def path(self):
        ruta=""
    @abstractmethod
    def links(self):
       link=""
    @abstractmethod
    def hipervinculos(self):
        hiper=""
    @abstractmethod
    def javaScrip(self):
        programaciopn=""
    @abstractmethod
    def diseños(self):
        descripcion=""
    @abstractmethod
    def redes_sociales (self):
        redes=[]
    @abstractmethod
    def imagenes (self):
        imagenes=[]
    @abstractmethod
    def contenido_de_texto(self):
        titulo=""
        Contenido=""
class website(page):
    def __init__(self) -> None:
        self.

