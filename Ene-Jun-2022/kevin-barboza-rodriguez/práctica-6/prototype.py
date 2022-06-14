import copy

class Oveja:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo
    
#prototipo concreto
class OvejaConcretePrototype(Oveja):

    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)

    def clone(self):
        return copy.copy(self)


if __name__ == "__main__":
    oveja_original = OvejaConcretePrototype('Dolly', 'droper')
    oveja_clon = oveja_original.clone()

    oveja_clon.set_nombre('Dolly_clon')

    print(f"nombre de la oveja: {oveja_original.get_nombre()}, tipo: {oveja_original.get_tipo()}")
    print(f"nombre de la oveja: {oveja_clon.get_nombre()}, tipo: {oveja_original.get_tipo()}")

