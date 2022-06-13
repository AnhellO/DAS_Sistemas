from __future__ import annotations
from abc import ABC, abstractmethod

# interface shape
class Shape(ABC):
    # metodos abtractos
    @abstractmethod
    def move(x,y) -> None:
        pass
    @abstractmethod
    def draw() -> None:
        pass
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

#clase Dot hereda de shape
class Dot(Shape):
    def __init__(self,id:str,x:int,y:int) -> None:
        self.id = id
        self.x = x
        self.y = y
        
    def move(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        return f"Dot '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, visitor: Visitor) -> None:
        visitor.dotV(self)

#clase circle hereda de shape
class Circle(Shape):
    def __init__(self,id:str,x:int,y:int,radius:int) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        
    def move(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        return f"Circle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, visitor: Visitor) -> None:
        visitor.circleV(self)

#clase Rectangle hereda de shape
class Rectangle(Shape):
    def __init__(self,id:str,x:int,y:int,width:int,height:int) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def move(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        return f"Rectangle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, visitor: Visitor) -> None:
        visitor.retangleV(self)


# interface visitor
class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, element: Dot) -> None:
        pass

    @abstractmethod
    def visit_circle(self, element: Circle) -> None:
        pass
    
    @abstractmethod
    def visit_rectangle(self, element: Rectangle) -> None:
        pass

# clase XMLExportVisitor hereda de visitor 
class XMLExportVisitor(Visitor):
    def visit_dot(self, dot:Dot) -> None:
        return f"XML export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"

    def visit_circle(self, circle:Circle) -> None:
        return f"XML export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
    
    def visit_rectangle(self, rectangle:Rectangle) -> None:
        return f"XML export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"

# clase JSONExportVisitor hereda de visitor
class JSONExportVisitor(Visitor):
    def visit_dot(self, dot:Dot) -> None:
        return f"JSON export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"

    def visit_circle(self, circle:Circle) -> None:
        return f"JSON export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
    
    def visit_rectangle(self, rectangle:Rectangle) -> None:
        return f"JSON export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"
# clase YAMLExportVisitor hereda de visitor
class YAMLExportVisitor(Visitor):
    def visit_dot(self, dot:Dot) -> None:
        return f"YAML export done for: <{dot.id} coordinates=({dot.x}, {dot.y})>"

    def visit_circle(self, circle:Circle) -> None:
        return f"YAML export done for: <{circle.id} radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
    
    def visit_rectangle(self, rectangle:Rectangle) -> None:
        return f"YAML export done for: <{rectangle.id} width={rectangle.width} height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"

def main():
    dot = Dot('dot-1', 5, 6)
    dot.move(10, 10)
    dotprint = dot.draw()
    print(dotprint)
    print()
    circle = Circle('circle-1', 2, 2, 5)
    circle.move(8, 4)
    circleprint = circle.draw()
    print(circleprint)
    print()
    rectangle = Rectangle('rectangle-1', -5, -8, 4, 6)
    rectangle.move(-5, 8)
    rectangleprint = rectangle.draw()
    print(rectangleprint)
    print()
    dot = Dot('dot-xml', 10, 6)
    circle = Circle('circle-xml', 6, 2, 3)
    rectangle = Rectangle('rectangle-xml', -5, 10, 5, 8)
    xml_visitor = XMLExportVisitor()
    print(xml_visitor.visit_dot(dot))
    print(xml_visitor.visit_dot(circle))
    print(xml_visitor.visit_dot(rectangle))
    print()
    dot = Dot('dot-json', 10, 6)
    circle = Circle('circle-json', 6, 2, 3)
    rectangle = Rectangle('rectangle-json', -5, 10, 5, 8)
    json_visitor = JSONExportVisitor()
    print(json_visitor.visit_dot(dot))
    print(json_visitor.visit_dot(circle))
    print(json_visitor.visit_dot(rectangle))
    print()
    dot = Dot('dot-yaml', 10, 6)
    circle = Circle('circle-yaml', 6, 2, 3)
    rectangle = Rectangle('rectangle-yaml', -5, 10, 5, 8)
    yaml_visitor = YAMLExportVisitor()
    print(yaml_visitor.visit_dot(dot))
    print(yaml_visitor.visit_dot(circle))
    print(yaml_visitor.visit_dot(rectangle))
    
    
if __name__ == "__main__":
    main()