from Persona import Persona
class Cliente(Persona):
    def __init__(self, nombre, apellidos, edad, direccion, telefono, idCliente):
        Persona.__init__(self, nombre, apellidos, edad, direccion, telefono)
        self.idCliente = idCliente

    def getIdCliente(self):
        return self.idCliente
    def setidCliente(self):
        self.idCliente = idCliente

    def atribCliente(self):
        return "Nombre: {}\nApellidos: {}\nEdad: {}\nDirección {}\nTeléfono: {}\nNúmero de Cliente: {}\n".format(self.nombre,
        self.apellidos, self.edad, self.direccion, self.telefono, self.idCliente)
