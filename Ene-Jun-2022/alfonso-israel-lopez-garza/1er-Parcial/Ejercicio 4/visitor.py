from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):
    '''Interfaz Visitor con metodos abstractos'''
    @abstractmethod
    def visit_dot(d: Dot):
        pass

    @abstractmethod
    def visit_circle(c: Circle):
        pass

    @abstractmethod
    def visit_rectangle(r: Rectangle):
        pass
    
    @abstractmethod
    def visit_compoundGraphic(cs: CompoundShape):
        pass

class Shape(ABC):
    @abstractmethod
    def move(self, x,y):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accept(v: Visitor):
        pass

class Dot(Shape):
    '''Forma Dot'''
    def __init__(self,id,x,y) -> None:
        self.id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Dot '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    def accept(v: Visitor):
        pass

class Circle(Shape):
    '''Forma Circle'''
    def __init__(self,id,x,y,radius) -> None:
        self.id = id
        self.x= x
        self.y = y
        self.radius = radius
    
    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Circle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"
    
    def accept(v: Visitor):
        pass

class Rectangle(Shape):
    '''Forma Rectangle'''
    def __init__(self,id,x,y,width, height) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Rectangle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    def accept(v: Visitor):
        pass

class XMLExportVisitor(Visitor):
    '''Exportando en XML las diferentes Formas'''
    def visit_dot(self,d: Dot):
        return f"XML export done for: <{d.id} coordinates=({d.x}, {d.y})>"

    def visit_circle(self,c: Circle):
        return f"XML export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"

    def visit_rectangle(self,r: Rectangle):
        return f"XML export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"


class JSONExportVisitor(Visitor):
    '''Exportando en JSON las diferentes formas.'''
    def visit_dot(self, d: Dot):
        return f"JSON export done for: <{d.id} coordinates=({d.x}, {d.y})>"
    
    def visit_circle(self, c: Circle):
        return f"JSON export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"
    
    def visit_rectangle(self, r: Rectangle):
        return f"JSON export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"
    

class YAMLExportVisitor(Visitor):
    '''Exportando en YAML las diferentes formas.'''
    def visit_dot(self, d: Dot):
        return f"YAML export done for: <{d.id} coordinates=({d.x}, {d.y})>"

    def visit_circle(self, c: Circle):
        return f"YAML export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"

    def visit_rectangle(self, r: Rectangle):
        return f"YAML export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"
