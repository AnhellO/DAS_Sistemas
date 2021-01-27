import copy


class Oveja(object):
    """docstring for Oveja"""

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}'


if __name__ == '__main__':
    original = Oveja('Dolly - [Original]', 'Merina de Aries')
    print(original)
    print('')

    clon = copy.copy(original)
    clon.nombre = 'Skiry - [Clon]'
    clon.tipo = 'Merina de Aries'
    print(clon)
