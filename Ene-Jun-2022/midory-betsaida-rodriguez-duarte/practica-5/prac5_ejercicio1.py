from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

    # las clases deben de tener los mismo metodos que la interfaz de lo contrario
    # no funcionan.

class Triangulo(Polygon):
    def num_of_sides(self):
        return "Es un triangulo, que cuena con 3 lados."

class Cuadraro(Polygon):
    def num_of_sides(self):
        return "Es un cuadrado, que cuenta con 4 lados."

class Pentagono(Polygon):
    def num_of_sides(self):
        return "Es un pentagono, que cuenta con 5 lados."

class Hexagono(Polygon):
    def num_of_sides(self):
        return "Es un hexagano, que cuenta con 6 lados."

