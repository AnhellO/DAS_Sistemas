from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

    # las clases deben de tener los mismo metodos que la interfaz 

class Triangulo(Polygon):
    def num_of_sides(self):
        return "Es un triangulo3 lados."

class Cuadraro(Polygon):
    def num_of_sides(self):
        return "Es un cuadrado 4 lados."

class Pentagono(Polygon):
    def num_of_sides(self):
        return "Es un pentagono 5 lados."

class Hexagono(Polygon):
    def num_of_sides(self):
        return "Es un hexagano 6 lados."
        