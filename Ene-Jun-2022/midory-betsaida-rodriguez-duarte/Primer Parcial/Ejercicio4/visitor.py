from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_dot(self):
        pass
    @abstractmethod
    def visit_circle(self):
        pass
    @abstractmethod
    def visit_rectangle(self):
        pass

class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        return f"XML export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"
    
    def visit_circle(self, circle: Circle):
        return f"XML export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"

    def visit_rectangle(self, rectangle : Rectangle):
        return f"XML export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"



class JSONExportVisitor(Visitor):
    def visit_dot(self, dot : Dot):
        return f"JSON export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"
    
    def visit_circle(self, circle : Circle):
        return f"JSON export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"

    def visit_rectangle(self,rectangle : Rectangle):
        return f"JSON export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"

class YAMLExportVisitor(Visitor):
    def visit_dot(self,dot : Dot):
        return f"YAML export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"
    
    def visit_circle(self,circle : Circle):
        return f"YAML export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"

    def visit_rectangle(self, rectangle : Rectangle):
        return f"YAML export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"


class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def move():
        pass
    @abstractmethod
    def draw():
        pass
    @abstractmethod
    def accept():
        pass

class Dot(Shape):
    def __init__(self,id,x,y) -> None:
        self.id = id
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Dot '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    def accept():
        pass

class Circle(Shape):
    def __init__(self, id ,x ,y ,radius) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Circle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    def accept():
        pass

class Rectangle(Shape):
    def __init__(self,id ,x ,y ,width ,height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Rectangle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    def accept():
        pass





    