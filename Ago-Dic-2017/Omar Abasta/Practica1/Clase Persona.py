class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def getNombre(self):
        return self.nombre

    def getApellidoPaterno(self):
        return self.apellidoPaterno

    def getApellidoMaterno(self):
        return self.apellidoMaterno

    def getEdad(self):
        return self.edad

    def getDomicilio(self):
        return self.domicilio

    def getTelefono(self):
        return self.telefono
