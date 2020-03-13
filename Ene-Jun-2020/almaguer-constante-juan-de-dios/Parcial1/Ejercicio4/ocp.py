class Animal:
    def _init_(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        pass

    def sonido(self) -> str:
        pass


# se crean clases para los distintosanimales
class Perro(Animal):
    def sonido(self):
        return 'guau'


class Gato(Animal):
    def sonido(self):
        return 'miaun'


def sonido(animales: list):
    for animal in animales:
        print(animal.sonido())


animales = [Animal('Perro'), Animal('Gato')]

sonido(animales)
