from abc import ABC,abstractmethod
class Pedido():
    def __init__(self,nombre,capa_base,salsas,condimentos,sasonadores,capas):
        self.nombre=nombre
        self.capa_base=capa_base
        self.salsas=salsas
        self.condimentos=condimentos
        self.sasonadores=sasonadores
        self.capas=capas

class AbstractPedido(ABC):
    @abstractmethod
    def get_Pedido(self,url):
        pass
class cliente():
    def __init__(self,name,email,phone,picture,location):
        self.name=name
        self.email=email
        self.phone=phone
        self.picture=picture
        self.location=location
class AbstracClient(ABC):
    @abstractmethod
    def get_usuario(self,url):
        pass

class AbstractbasePedidos(ABC):
    @abstractmethod
    def insertarPedido_db(self,id_Pedido,Pedido):
        pass
    @abstractmethod
    def insertarCliente_db(self,id_cliente,cliente):
        pass
    @abstractmethod
    def insertarOrden_db(self,id_orden,total,fecha,tipo,id_Pedido,id_user):
        pass
    @abstractmethod
    def selectPedido(self):
        pass
    @abstractmethod
    def deleteOrden(self,id_orden):
        pass
    @abstractmethod
    def selectOrden(self,id):
        pass
    @abstractmethod
    def selectCliente(self,id):
        pass
