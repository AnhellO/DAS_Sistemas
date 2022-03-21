#DAS 8vo semestre
#Parcial 1, E: 3 Factory Method
#Interface & Instances

import abc

class polygon(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self):
        self.Type = "Dot"
    
    @abc.abstractmethod
    def getType(self):
        pass
    
class Triangle(polygon):
    
    def __init__(self):
        self.Type = "Triangle"
        
    def getType(self):
        return self.Type
    
class Square(polygon):
    
    def __init__(self):
        self.Type = "Square"
        
    def getType(self):
        return self.Type
    
class Pentagon(polygon):
    
    def __init__(self):
        self.Type = "Pentagon"
        
    def getType(self):
        return self.Type