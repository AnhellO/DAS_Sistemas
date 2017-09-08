from Persona import Persona

class Cliente(Persona):
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono,idCliente):
        super().__init__(nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono)
        self.idCliente = idCliente

    def getIDCliente(self):
        return self.idCliente

    def setIDClient(self,idCliente):
        self.idCliente = idCliente

Cliente1 = ('Francisco','Flores','Martinez','Masculio','27','en su casa :v','4568271','001')
