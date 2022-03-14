from abc import ABC, abstractmethod
 
class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

class triangulo(Polygon):

    def num_of_sides(self):
        return "El triangulo tiene 3 lados"

class cuadrado(Polygon):

    def num_of_sides(self):
        return "El cuadrado tiene 4 lados"

class pentagono(Polygon):

    def num_of_sides(self):
        return "El pentagono tiene 5 lados"

class hexagono(Polygon):
    
    def num_of_sides(self):
        return "El hexagono tiene 6 lados"
        
if __name__ == '__main__':
    triangulo_1 = triangulo()
    cuadrado_1 = cuadrado()
    pentagono_1 = pentagono()
    hexagono_1 = hexagono()