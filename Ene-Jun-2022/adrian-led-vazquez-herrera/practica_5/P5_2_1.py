#DAS Práctica 5.2.1

from abc import ABC, abstractmethod
 
class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass
    
class Triangle(Polygon):
    
    def __init__(self):
        self.sides=3
    
    def num_of_sides(self):
        return self.sides

class Square(Polygon):
    
    def __init__(self):
        self.sides=4
    
    def num_of_sides(self):
        return self.sides
    
class Pentagon(Polygon):
    
    def __init__(self):
        self.sides=5
    
    def num_of_sides(self):
        return self.sides
    
class Hexagon(Polygon):
    
    def __init__(self):
        self.sides=6
    
    def num_of_sides(self):
        return self.sides
  

T=Triangle()
S=Square()
P=Pentagon()
H=Hexagon()
shapes=[T,S,P,H]
for shape in shapes:
    print(shape.num_of_sides())
        