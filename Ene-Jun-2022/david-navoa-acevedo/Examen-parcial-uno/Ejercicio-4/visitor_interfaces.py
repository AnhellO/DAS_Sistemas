from abc import ABC,abstractclassmethod

#Clases Dot, Circle, Rectangle vacias, estas clases estan aquí ya que 
#cada methodo abstracto de la interface Visitor reciben un objeto de Dot, Circle, Rectangle
#correspondientemente. Estan vacias ya que solo necesita recibir el Objeto como tal, no hacer nada con el

class Dot:
    pass
class Circle:
    pass
class Rectangle:
    pass
#Interfaz visitor
class Visitor(ABC):
    
    @abstractclassmethod
    def visit_dot(self, element = Dot):
        pass
    @abstractclassmethod
    def visit_circle(self, element = Circle):
        pass
    @abstractclassmethod
    def visit_rectangle(self, element = Rectangle):
        pass
#Interface Shape
class Shape(ABC):
    
    @abstractclassmethod
    def move(x, y):
        pass
    @abstractclassmethod
    def draw():
        pass
    @abstractclassmethod
    def accept(v: Visitor):
        pass