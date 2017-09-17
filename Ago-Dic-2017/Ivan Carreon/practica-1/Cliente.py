from Persona import Persona

class Cliente(Persona):
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono,idCliente):
        super().__init__(nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono)
        self.idCliente = idCliente

    def getIDCliente(self):
        return self.idCliente

    def setIDClient(self,idCliente):
        self.idCliente = idCliente

Cliente1 = Cliente('Francisco','Flores','Martinez','Masculio','27','en su casa :v','4568271','001')
Cliente2 = Cliente('Daniela','Lopez','Malacara','Femenino','35','cerca del monte :v','8447469523','002')
Cliente3 = Cliente('Rosa Maria','Juarez','Medina','Femenino','24','en tu kora :v' ,'1723450','003')
