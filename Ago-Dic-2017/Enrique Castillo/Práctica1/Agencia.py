class Agencia:
    def __init__(self, nomAgencia, direccion):
        self.nomAgencia = nomAgencia
        self.direccion = direccion

    def getNomAgencia(self):
        return self.nomAgencia
    def setNomAgencia(self, nombrAgencia):
        self.nombrAgencia = nombrAgencia

    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion

    def atribAgencia(self):
        return "Agencia: {}\nDirección: {}\n".format(self.nomAgencia, self.direccion)
