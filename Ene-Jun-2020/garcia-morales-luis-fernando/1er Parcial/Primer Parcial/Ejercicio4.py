class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self):
        pass

    def sonido(self):
        pass

class Leon(Animal):
    def sonido():
        return "roar"

class Raton(Animal):
    def sonido():
        return "squeak"

def animal_sonido(animales: list):
    for i in animales:
        print(i.sonido())
animales = [
        Leon,
        Raton
    ]
animal_sonido(animales)