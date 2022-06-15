from abc import ABC, abstractmethod
 
class Polygon(ABC):
    @abstractmethod
    def __init__(self,nombre):
        self.nombre=nombre

    @abstractmethod
    def num_of_sides(self):
        pass

class triangulo(Polygon):
    def __init__(self, nombre):
        super().__init__(nombre)
    def num_of_sides(self):
        self.n_lados=3
        super().num_of_sides()


class cuadrado(Polygon):
    def __init__(self, nombre):
        super().__init__(nombre)
    def num_of_sides(self):
        self.n_lados=4
        super().num_of_sides()
    

class pentagono(Polygon):
    def __init__(self, nombre):
        super().__init__(nombre)
    def num_of_sides(self):
        self.n_lados=5
        super().num_of_sides()

class hexagono(Polygon):
    def __init__(self, nombre):
        super().__init__(nombre)
    def num_of_sides(self):
        self.n_lados=6
        super().num_of_sides()

