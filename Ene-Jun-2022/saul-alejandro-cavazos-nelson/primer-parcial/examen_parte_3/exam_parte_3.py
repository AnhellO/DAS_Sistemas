
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def getType(self)-> str:
       pass
    

class Triangle(Polygon):
    def getType(self) -> str:
        return "triangulo"
   
class Square(Polygon):
    def getType(self) -> str:
        return "cuadrado"
   

class Pentagon(Polygon):
    def getType(self) -> str:
        return "pentagono"
 

class client():
    def main(self):
        figura_1=PolygonFactory.getPolygon("T")
        print(figura_1().getType())
        figura_2=PolygonFactory.getPolygon("C")
        print(figura_2().getType())
        figura_3=PolygonFactory.getPolygon("P")
        print(figura_3().getType())

class PolygonFactory ():
    def getPolygon(figura):
        if figura=="T":
            return Triangle
        elif figura=="C":
            return Square
        elif figura=="P":
            return Pentagon
        
if __name__ == "__main__":
   client().main()