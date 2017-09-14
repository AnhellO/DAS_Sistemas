class Persona:
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,sexo,edad,domicilio,telefono):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.sexo = sexo
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def getNombre(self):
        return self.nombre
    def getApellidoPaterno(self):
        return self.apellidoPaterno
    def getApellidoMaterno(self):
        return self.apellidoMaterno
    def getSexo(self):
        return self.sexo
    def getEdad(self):
        return self.edad
    def getDomicilio(self):
        return self.domicilio
    def getTelefono(self):
        return self.telefono

    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellidoPaterno(self,apellidoPaterno):
        self.apellidoPaterno = apellidoPaterno
    def setApellidoMaterno(self,apellidoMaterno):
        self.apellidoMaterno = apellidoMaterno
    def setSexo(self,sexo):
        self.sexo = sexo
    def setEdad(self,edad):
        self.edad = edad
    def setDomicilio(self,domicilio):
        self.domicilio = domicilio
    def setTelefono(self,telefono):
        self.telefono = telefono
