import copy

class Oveja:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo

    def get_tipo(self):
        return self.tipo

    def __copy__(self):
        nombre = copy.copy(self.nombre)
        tipo = copy.copy(self.tipo)

        new = self.__class__(
            nombre,tipo
        )
        new.__dict__.update(self.__dict__)
        return new
