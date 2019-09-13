from abc import ABC,abstractmethod
class Tako():
    def __init__(self,nombre,principal,salsas,condimentos,sasonadores,shell):
        self.nombre=nombre
        self.principal=principal
        self.salsas=salsas
        self.condimentos=condimentos
        self.sasonadores=sasonadores
        self.shell=shell

class TakoAbstracto(ABC):
    @abstractmethod
    def get_tako(self,url):
        pass
class Cliente():
    def __init__(self,name,email,phone,picture,location):
        self.name=name
        self.email=email
        self.phone=phone
        self.picture=picture
        self.location=location
class ClienteAbstracto(ABC):
    @abstractmethod
    def get_cliente(self,url):
        pass

class BaseAbstracta(ABC):
    @abstractmethod
    def insertar_tako(self,id_tako,Tako):
        pass
    @abstractmethod
    def insertar_Cliente(self,id_Cliente,Cliente):
        pass
    @abstractmethod
    def insertar_Orden(self,id_orden,total,fecha,tipo,id_tako,id_user):
        pass
    @abstractmethod
    def select_tako(self):
        pass
    @abstractmethod
    def select_Cliente(self,id):
        pass
    @abstractmethod
    def select_Orden(self,id):
        pass
    @abstractmethod
    def delete_Orden(self,id_orden):
        pass
