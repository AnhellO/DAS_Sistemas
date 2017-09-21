from persona import Persona

class Vendedor(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono, numVendedor):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)
        self.numVendedor = numVendedor

    def getNumVendedor(self):
        return self.numVendedor
