from abc import ABC, abstractmethod

class Taco():
    def __init__(self,name,ingprincipal,salsas,condimentos,seasonings,cubierta):
        self.name=name
        self.ingprincipal=ingprincipal
        self.salsas=salsas
        self.condimentos=condimentos
        self.seasonings=seasonings
        self.cubierta=cubierta

class AbstractTaco(ABC):
    @abstractmethod
    def get_taco(self,url):
        pass

class Cliente():
    def __init__(self,name,email,location,phone,picture):
        self.name=name
        self.email=email
        self.location=location
        self.phone=phone
        self.picture=picture

class AbstractCliente(ABC):
    @abstractmethod
    def get_cliente(self,url):
        pass

class AbstractBDTacos(ABC):
    @abstractmethod
    def insertarBDTacos(self,id_taco,Taco):
        pass

    @abstractmethod
    def insertarBDCliente(self,id_cliente,Cliente):
        pass

    @abstractmethod
    def insertarBDOrden(self,id_orden,total,fecha,id_taco,id_cliente):
        pass

    @abstractmethod
    def deleteOrden(self,id_orden):
        pass

    @abstractmethod
    def selectTaco(self):
        pass

    @abstractmethod
    def selectOrden(self,id_orden):
        pass

    @abstractmethod
    def selectCliente(self,id_cliente):
        pass
