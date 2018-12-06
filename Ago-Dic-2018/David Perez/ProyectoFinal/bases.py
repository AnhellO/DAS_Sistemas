from abc import ABC,abstractmethod
class Taco():
    def __init__(self,nombre,capa_base,salsas,condimentos,sasonadores,capas):
        self.nombre=nombre
        self.capa_base=capa_base
        self.salsas=salsas
        self.condimentos=condimentos
        self.sasonadores=sasonadores
        self.capas=capas

class AbstractTaco(ABC):
    @abstractmethod
    def get_taco(self,url):
        pass
class cliente():
    def __init__(self,name,email,picture,phone,location):
        self.name=name
        self.email=email
        self.phone=phone
        self.picture=picture
        self.location=location
class AbstracClient(ABC):
    @abstractmethod
    def get_usuario(self,url):
        pass

class AbstractbaseTacos(ABC):
    @abstractmethod
    def insertarTaco_db(self,id_taco,Taco):
        pass
    @abstractmethod
    def insertarCliente_db(self,id_cliente,cliente):
        pass
    @abstractmethod
    def insertarOrden_db(self,id_orden,total,fecha,tipo,id_taco,id_user):
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
