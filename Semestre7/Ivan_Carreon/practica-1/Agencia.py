class Agencia:
    def __init__(self,nombre,direccion,email):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email

    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getEmail(self):
        return self.email

    def setNombre(self,nombre):
        self.nombre = nombre
    def setDireccion(self,direccion):
        self.direccion = direccion
    def setEmail(self,email):
        self.email = email

    def ventaVehiculo(self,Cliente,Vehiculo,Vendedor):
        return Cliente+" "+Vehiculo+" "+Vendedor

Sagencia = Agencia('El Horizonte \n S.A. de C.V.','Balcones de buenavista #193','elhorizonte@outlook.com')
