from abc import ABC,abstractmethod
class Taquito():
    def __init__(self,nombre,relleno,salsas,condimentos,sasonadores,cubierta):
        self.nombre=nombre
        self.relleno=relleno
        self.salsas=salsas
        self.condimentos=condimentos
        self.sasonadores=sasonadores
        self.cubierta=cubierta

class AbstractTaquitos(ABC):
    @abstractmethod
    def get_taquito(self,url):
        pass
