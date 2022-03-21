from __future__ import annotations
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def move(x,y) -> None:
        pass
    @abstractmethod
    def draw() -> None:
        pass
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    class Dot(Shape):
        def __init__(self,id:str,x:int,y:int) -> None:
            self.id = id
            self.x = x
            self.y = y

    def move(self,x,y)-> None:
        
        self.x =x
        self.y =y

    def draw(self) -> None:
        return f"Dot"

class Circle(Shape):
    def __init__(self,id:str,x:int,y:int,radius:int) -> None:
        self.id =id
        self.x =x
        self.y =y
        self.radius = radius

    def move(self, x, y) -> None:
        self.x=x
        self.y=y

class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, element: Dot) ->None:
        pass
    @abstractmethod
    def visit_circle(self, element: Circle)->None:
        pass

    class XMLExportVisitor(Visitor):
        def visit_dot(self, element: Dot) ->None:
            return f"XML"

        def visit_circle(self, element: Circle)->None:
            return f"XML"

class JSONExportVisitor(Visitor):
        def visit_dot(self, element: Dot) ->None:
            return f"JSONE"

        def visit_circle(self, element: Circle)->None:
            return f"JSONE"

class YAMLExportVisitor(Visitor):
        def visit_dot(self, element: Dot) ->None:
            return f"YAML"
        def visit_circle(self, element: Circle)->None:
            return f"YAML"


