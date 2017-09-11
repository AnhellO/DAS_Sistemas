class Persona:
    # Definicion de __init__ y atributos de la clase Persona
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        # Se inician atributos
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    # Metodo getNombre
    def getNombre(self):
        return self.nombre

    # Metodo getApellidoPaterno
    def getApellidoPaterno(self):
        return self.apellidoPaterno

    # Metodo getApellidoMaterno
    def getApellidoMaterno(self):
        return self.apellidoMaterno

    # Metodo getEdad
    def getEdad(self):
        return self.edad

    # Metodo getDomicilio
    def getDomicilio(self):
        return self.domicilio

    # Metodo getTelefono
    def getTelefono(self):
        return self.telefono

    # informePersona regresa un string con los datos de Persona, el cual será usado
    # en las clases hijo donde se agregarán los datos faltantes
    def informePersona(self):
        return "Nombre: {0} {1} {2}\nEdad: {3}\nDomicilio: {4}\nTelefono: {5}".format(self.nombre,
                            self.apellidoPaterno, self.apellidoMaterno, self.edad,
                             self.domicilio, self.telefono)
