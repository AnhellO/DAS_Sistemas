from Persona import Persona
class Vendedor(Persona):
    def __init__(self, nombre, apellidos, edad, direccion, telefono, idVendedor):
        Persona.__init__(self, nombre, apellidos, edad, direccion, telefono)
        self.idVendedor = idVendedor

    def getIdVendedor(self):
        return self.idVendedor
    def setidVendedor(self):
        self.idVendedor = idVendedor

    def atribVendedor(self):
        return "Nombre: {}\nApellidos: {}\nEdad: {}\nDirección {}\nTeléfono: {}\nNúmero de Vendedor: {}\n".format(self.nombre,
        self.apellidos, self.edad, self.direccion, self.telefono, self.idVendedor)
