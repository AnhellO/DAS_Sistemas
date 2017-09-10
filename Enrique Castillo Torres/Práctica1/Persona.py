class Persona:
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos
    def setMarca(self,apellidos):
        self.apellidos = apellidos

    def getEdad(self):
        return self.edad
    def setEdad(self,edad):
        self.edad = edad

    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.Telefono
    def setTelefono(self,telefono):
        self.telefono = telefono

    def atribPersona(self):
        return "Nombre: {}\nApellidos: {}\nEdad: {}\nDirección: {}\nTeléfono: {}\n".format(self.nombre,
        self.apellidos, self.edad, self.direccion, self.telefono)
