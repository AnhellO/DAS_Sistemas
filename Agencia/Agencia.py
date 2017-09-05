class Agencia:
    # Clase para representar una agencia de carros.

    def __init__(self, nombre_agencia, concesionaria, direccion, rfc):
        # Inicializa atributos para describir la agencia.
        self.nombre_agencia = nombre_agencia
        self.concesionaria = concesionaria
        self.direccion = direccion
        self.rfc = rfc

    def get_nombre_agencia(self):
        # Regresa el nombre de la agencia.
        return self.nombre_agencia

    def set_nombre_agencia(self, nombre_agencia):
        # Asigna un nombre a la agencia.
        self.nombre_agencia = nombre_agencia

    def get_concesionaria(self):
        # Regresa el nombre de la concesionaria.
        return self.concesionaria

    def set_concesionaria(self, concesionaria):
        # Asigna un nombre a la concesionaria.
        self.concesionaria = concesionaria

    def get_direccion(self):
        # Regresa la dirección.
        return self.direccion

    def set_direccion(self, direccion):
        # Asigna otra dirección.
        self.direccion = direccion

    def get_rfc(self):
        # Regresa la dirección.
        return self.rfc

    def set_rfc(self, rfc):
        # Asigna otro RFC.
        self.rfc = rfc

    def get_info_agencia(self):
        # Regresa la información de una agencia.
        info = "Agencia: {}\nConcesionaria: {}\nDirección: {}\nRFC: {}".format(self.nombre_agencia,
        self.concesionaria, self.direccion, self.rfc)
        return(info)

mi_agencia = Agencia('Rivero Motors', 'Chevrolet', 'Miguel Alemán 5400 Col. Torres de Lindavista',
'SHDFS238RY28')
print(mi_agencia.get_info_agencia())
