from abc import ABC, abstractmethod
 
class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

class Triangulo(Polygon):
    def num_of_sides(self):
        sides = "Number of sides: 3"
        return sides
class Cuadrado(Polygon):
    def num_of_sides(self):
        sides = "Number of sides: 4"
        return sides

class Pentagono(Polygon):
    def num_of_sides(self):
        sides = "Number of sides: 5"
        return sides

class Hexagono(Polygon):
    def num_of_sides(self):
        sides = "Number of sides: 6"
        return sides

if __name__ == "__main__":
    triangulo = Triangulo()
    cuadrado = Cuadrado()
    pentagono = Pentagono()
    hexagono = Hexagono()

    print(triangulo.num_of_sides())
    print(cuadrado.num_of_sides())
    print(pentagono.num_of_sides())
    print(hexagono.num_of_sides())
