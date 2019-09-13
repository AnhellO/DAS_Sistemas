from abc import ABC,abstractmethod
class Abstract_Base_la_dvd(ABC):
    @abstractmethod
    def insert_Taco_db(self,id_taco,Taquito):
        pass
    @abstractmethod
    def insert_User_db(self,id_user,Users):
        pass
    @abstractmethod
    def insert_Orden_db(self,id_orden,total,fecha,tipo,id_taco,id_user):
        pass
    @abstractmethod
    def delete_Orden(self,id_orden):
        pass
    @abstractmethod
    def select_Orden(self,id_orden):
        pass
    @abstractmethod
    def select_User(self):
        pass
    @abstractmethod
    def select_Taquitos(self):
        pass
    @abstractmethod
    def select_user_id(self,id_cliente):
        pass
