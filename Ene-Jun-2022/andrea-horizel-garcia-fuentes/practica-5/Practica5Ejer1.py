from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

    # Estas clases deben de tener metodos igual o de lo contrario no funcionaran.

class Triangulo(Polygon):
    def num_of_sides(self):
        return "Triangulo que cuenta con 3 lados"

class Cuadraro(Polygon):
    def num_of_sides(self):
        return "Cuadrado que cuenta con 4 lados"

class Pentagono(Polygon):
    def num_of_sides(self):
        return "Pentagono que cuenta con 5 lados."

class Hexagono(Polygon):
    def num_of_sides(self):
        return "Hexagano que cuenta con 6 lados."

