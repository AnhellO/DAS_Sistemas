from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass


class Triangulo(Polygon):
    def num_of_sides(self):
        return "Triangulo tiene tres lados"

class Cuadraro(Polygon):
    def num_of_sides(self):
        return "Cuadrado tiene cuatro lados"

class Pentagono(Polygon):
    def num_of_sides(self):
        return "Pentagono tiene cinco lados"

class Hexagono(Polygon):
    def num_of_sides(self):
        return "Hexagono tiene seis lados"