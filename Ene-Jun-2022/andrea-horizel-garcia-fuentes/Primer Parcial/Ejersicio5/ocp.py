from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def rugir(self):
        pass


class Leon(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def rugir(self):
        return 'Roar'


class Raton(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def rugir(self):
        return 'Squeak'


if __name__ == '__main__':
    raton = Raton("Ratón")
    leon = Leon("Leon")
    animales = [raton, leon]

    for animal in animales:
        print(animal.rugir())

#Respuesta de la pregunta sobre el codigo:Puede pasar que el codigo sea dificil de arreglar por la complejidad.