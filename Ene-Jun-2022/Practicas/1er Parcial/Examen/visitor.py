from __future__ import annotations
import abc

# Element interface
class Shape(metaclass=abc.ABCMeta):
    def __init__(self, id: str, x: int, y: int) -> None:
        self.id = id
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    @abc.abstractmethod
    def draw(self) -> str:
        pass
    
    @abc.abstractmethod
    def accept(self, v: Visitor) -> str:
        pass
    
    def __str__(self) -> str:
        return f"<{self.id} coordinates=({self.x}, {self.y})>"

# Concrete Element A
class Dot(Shape):
    def draw(self) -> str:
        return f"{__class__.__name__} '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, v: Visitor) -> str:
        return v.visit_dot(self)
    
    def __str__(self) -> str:
        return super().__str__()

# Concrete Element B
class Circle(Shape):
    def __init__(self, id: str, x: int, y: int, radius: int) -> None:
        super().__init__(id, x, y)
        self.radius = radius
        
    def draw(self) -> str:
        return f"{__class__.__name__} '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, v: Visitor) -> str:
        return v.visit_circle(self)
    
    def __str__(self) -> str:
        return f"<{self.id} radius={self.radius} coordinates=({self.x}, {self.y})>"

# Concrete Element C
class Rectangle(Shape):
    def __init__(self, id: str, x: int, y: int, width: int, height: int) -> None:
        super().__init__(id, x, y)
        self.width = width
        self.height = height

    def draw(self) -> str:
        return f"{__class__.__name__} '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(self, v: Visitor) -> str:
        return v.visit_rectangle(self)
    
    def __str__(self) -> str:
        return f"<{self.id} width={self.width} height={self.height} coordinates=({self.x}, {self.y})>"

# Visitor interface
class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_dot(self, dot: Dot) -> str:
        pass
    
    @abc.abstractmethod
    def visit_circle(self, circle: Circle) -> str:
        pass
    
    @abc.abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> str:
        pass

# Concrete Visitor A
class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot) -> str:
        return f"XML export done for: {dot}"
    
    def visit_circle(self, circle: Circle) -> str:
        return f"XML export done for: {circle}"
    
    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f"XML export done for: {rectangle}"

# Concrete Visitor B
class JSONExportVisitor(Visitor):
    def visit_dot(self, dot: Dot) -> str:
        return f"JSON export done for: {dot}"
    
    def visit_circle(self, circle: Circle) -> str:
        return f"JSON export done for: {circle}"
    
    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f"JSON export done for: {rectangle}"

# Concrete Visitor C
class YAMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot) -> str:
        return f"YAML export done for: {dot}"
    
    def visit_circle(self, circle: Circle) -> str:
        return f"YAML export done for: {circle}"
    
    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f"YAML export done for: {rectangle}"
