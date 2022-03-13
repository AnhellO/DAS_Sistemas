from abc import ABC, abstractmethod
 
class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        print('Number of sides:')

class Triangulo(Polygon):
    
    def num_of_sides(self):
        super().num_of_sides()
        print('three sides\n')

class Cuadrado(Polygon):
    def num_of_sides(self):
        super().num_of_sides()
        print('four sides\n')

class Pentagono(Polygon):
    def num_of_sides(self):
        super().num_of_sides()
        print('five sides\n')

class Hexagono(Polygon):
    def num_of_sides(self):
        super().num_of_sides()
        print('six sides\n')

if __name__ == "__main__":
    triangulo = Triangulo()
    triangulo.num_of_sides()

    cuadrado = Cuadrado()
    cuadrado.num_of_sides()

    pentagono = Pentagono()
    pentagono.num_of_sides()

    hexagono = Hexagono()
    hexagono.num_of_sides()