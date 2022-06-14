import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Oveja(Prototype):
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
        return f"La oveja {self.nombre} de tipo {self.tipo}"

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    dolly = Oveja('Dolly', 'Dorper')
    dolly_clon = dolly.clone()
    print(dolly)

    print("\nDolly clon:")
    print(dolly_clon)

    print("\nDolly clon - Oveja tipo Dextel")
    dolly_clon.set_tipo('Dextel')
    print(dolly_clon)
