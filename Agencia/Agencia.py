class Agencia:
    # Clase para representar una agencia de carros.

    def __init__(self, nombre, concesionaria, direccion, rfc):
        # Inicializa atributos para describir la agencia.
        self.nombre = nombre
        self.concesionaria = concesionaria
        self.direccion = direccion
        self.rfc = rfc

    def getNombre(self):
        # Regresa el nombre de la agencia.
        return self.nombre

    def setNombre(self, nombre):
        # Asigna un nombre a la agencia.
        self.nombre = nombre

    def getConcesionaria(self):
        # Regresa el nombre de la concesionaria.
        return self.concesionaria

    def setConcesionaria(self, concesionaria):
        # Asigna un nombre a la concesionaria.
        self.concesionaria = concesionaria

    def getDireccion(self):
        # Regresa la dirección.
        return self.direccion

    def setDireccion(self, direccion):
        # Asigna otra dirección.
        self.direccion = direccion

    def getRFC(self):
        # Regresa la dirección.
        return self.rfc

    def setRFC(self, rfc):
        # Asigna otro RFC.
        self.rfc = rfc

    def getInfoAgencia(self):
        # Regresa la información de una agencia.
        info = "Agencia: {}\nConcesionaria: {}\nDirección: {}\nRFC: {}"
            .format(self.nombre, self.concesionaria, self.direccion, self.rfc)
        return(info)
