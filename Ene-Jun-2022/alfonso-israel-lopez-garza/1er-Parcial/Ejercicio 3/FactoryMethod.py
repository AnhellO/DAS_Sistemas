from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def getType(Self):
        pass

class Trigle(Polygon):
    def getType(Self):
        return "Triangulo"

class Square(Polygon):
    def getType(Self):
        return "Cuadrado"

class Pentagon(Polygon):
    def getType(Self):
        return "Pentagono"

class PolygonFactory(object):
    @abstractmethod
    def getPolygon(self) ->Polygon:
        pass

    def figura(self):
        figura = self.getPolygon()
        poligono = figura.getType()
        return poligono

class ConcreteTriangle(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return Trigle()
        
class ConcreteSquare(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return Square()
        
class ConctretePentagon(PolygonFactory):
    def getPolygon(self) -> Polygon:
        return Pentagon()
        
def Cliente(poligono: PolygonFactory):
    return poligono.figura()

def main(lados):
    i = lados
    if i>2 and i<6:
        if i == 3:
            print(Cliente(ConcreteTriangle()))
        if i == 4:
            print(Cliente(ConcreteSquare()))
        if i == 5:
            print(Cliente(ConctretePentagon()))
    else:
        return "Error"

if __name__ == "__main__":
    lados = 3
    main(lados) # Segun los lados imprime la forma