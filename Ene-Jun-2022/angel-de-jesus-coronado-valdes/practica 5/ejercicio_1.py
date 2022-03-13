from abc import ABC, abstractmethod
 
class Polygon(ABC):
    
    @abstractmethod
    def num_of_sides(self):
        pass


class Triangle(Polygon):
    def num_of_sides(self):
        print("Sides of Triangle: 3") 
		
		
class Square(Polygon):
    def num_of_sides(self):
        print("Sides of Square: 0")
		
		
class Pentagon(Polygon):
    def num_of_sides(self):
        print("Sidesof Pentagon: 5")
		

class Hexagon(Polygon):
    def num_of_sides(self):
        print("Sides of Hexagon: 5")


if __name__ == "__main__":
    Hexagon = Hexagon()
    Hexagon.num_of_sides()
    
    Triangle = Triangle()
    Triangle.num_of_sides()
    
    Square = Square()
    Square.num_of_sides()
    
    Pentagon = Pentagon()
    Pentagon.num_of_sides()
