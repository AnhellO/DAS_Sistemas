from __future__ import annotations
from abc import ABC, abstractmethod

class PolygonFactory(ABC):
    def create(self):
        figura = self.getPolygon()
        a = str(figura.getType())
        return a

    @abstractmethod
    def getPolygon(self) -> Polygon:
        pass

class Triangle(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return ConcreteTriangle()

class Square(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return ConcreteSquare()

class Pentagon(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return ConcretePentagon()

class Polygon(ABC):
    def create(self):
        pass

    @abstractmethod
    def getType(self) -> str:
        pass 

class ConcreteTriangle(Polygon):
    def getType(self) -> str:
        return "Esto es un triangulo"

class ConcreteSquare(Polygon):
    def getType(self) -> str:
        return "Esto es un cuadrado"

class ConcretePentagon(Polygon):
    def getType(self) -> str:
        return "Esto es un pentagono"

def Cliente(polygon : PolygonFactory):
    print(polygon.create())
    
def main():
    print("Triangulo:")
    Cliente(Triangle())

    print("Cuadrado:")
    Cliente(Square())

    print("Pentagono:")
    Cliente(Pentagon())


if __name__ == "__main__":
    main()


