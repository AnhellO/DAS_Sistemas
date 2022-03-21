from abc import ABC, abstractmethod

#creador
class polygonFactory(ABC):

    @abstractmethod
    def getType(self):
        pass

#interfaz
class polygon(polygonFactory):
    
    @abstractmethod
    def getType(self):
        pass

#producto concreto
class Triangle(polygon):
    def getType(self):
        return "Triangle"

class Square(polygon):
    def getType(self):
        return "Square"
    
class Pentagon(polygon):
    def getType(self):
        return "Pentagon"

#el metodo main actua como cliente 
def main():
    triangle = Triangle()
    print(triangle.getType())

    square = Square()
    print(square.getType())

    pentagon = Pentagon()
    print(pentagon.getType())

if __name__ == "__main__":
    main()    
