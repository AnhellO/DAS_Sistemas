from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

class Triangulo(Polygon):
    def num_of_sides(self) -> int:
        return 3

class Cuadrado(Polygon):
    def num_of_sides(self) -> int:
        return 4

class Pentagono(Polygon):
    def num_of_sides(self) -> int:
        return 5

class Hexagono(Polygon):
    def num_of_sides(self) -> int:
        return 6


clss = [Triangulo, Cuadrado, Pentagono, Hexagono]

for cl in clss:
    print(f"¿Es {cl.__name__} subclase de Polygon? : {issubclass(cl,Polygon)}")

print()

for cl in clss:
    o = cl()
    print(f"Número de lados para {cl.__name__} : {o.num_of_sides()}")