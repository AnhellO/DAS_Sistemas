from Persona import Persona

class Vendedor(Persona):
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono,idVendedor):
        super().__init__(nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono)
        self.idVendedor = idVendedor

    def getIDVendedor(self):
        return self.idVendedor

    def setIDVendedor(self,idVendedor):
        self.idVendedor = idVendedor

Vendedor1 = Vendedor('Carlos','Guerrero','Jaramillo','Masculino','31','saltillo 2000','8446795248','01')
Vendedor2 = Vendedor('Eduardo','Carranza','Lopez','Masculino','29','oceania','8447532159','02')
Vendedor3 = Vendedor('Alejandra','Montoya','Silva','Femenino','26','landin','8447845153','03')
