from __future__ import annotations
import abc

'''
Implementación del patrón visitor creado a base del suite de pruebas unitarias ya
creadas, las pruebas no se modificaron. 
'''

# Interface Elemento
class Shape(abc.ABC):
    def __init__(self,id:str,x:int,y:int) -> None:
        self.id = id
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):        
        return f"{self.__class__.__name__} '{self.id}' drew at coordinates -> ({self.x}, {self.y})"

    @abc.abstractmethod
    def accept(self,visitor: Visitor):
        pass

# Elemento Concreto, implemeta la interface Elemento
class Dot(Shape):        
    def accept(self, visitor: Visitor): # Sobrescribe el metodo accept, ya que debe de 
        visitor.visit_dot(self)         # especificar su metodo de visitor 

class Circle(Shape):
    def __init__(self,id:str,x:int,y:int ,radius:int) -> None:
        super().__init__(id,x,y)
        self.radius = radius 

    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self,id:str,x:int,y:int ,width:int,height:int) -> None:
        super().__init__(id,x,y)
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)

# Interface Visitor
class Visitor:
    @abc.abstractmethod
    def visit_dot(self,d: Dot):
        pass

    @abc.abstractmethod
    def visit_circle(self,c: Circle):
        pass

    @abc.abstractmethod
    def visit_rectangle(self,r: Rectangle):
        pass

# Visitor concreto, implementa interface Visitor
class XMLExportVisitor(Visitor):    

    # Sobrescribe los meódos para su tipo de formato
    def visit_dot(self,d: Dot):
        return f"XML export done for: <{d.id} coordinates=({d.x}, {d.y})>"
    
    def visit_circle(self,c: Circle):
        return f"XML export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"
    
    def visit_rectangle(self,r: Rectangle):
        return f"XML export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"

class JSONExportVisitor(Visitor):
    def visit_dot(self,d: Dot):
        return f"JSON export done for: <{d.id} coordinates=({d.x}, {d.y})>"
    
    def visit_circle(self,c: Circle):
        return f"JSON export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"
    
    def visit_rectangle(self,r: Rectangle):
        return f"JSON export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"

class YAMLExportVisitor:
    def visit_dot(self,d: Dot):
        return f"YAML export done for: <{d.id} coordinates=({d.x}, {d.y})>"
    
    def visit_circle(self,c: Circle):
        return f"YAML export done for: <{c.id} radius={c.radius} coordinates=({c.x}, {c.y})>"
    
    def visit_rectangle(self,r: Rectangle):
        return f"YAML export done for: <{r.id} width={r.width} height={r.height} coordinates=({r.x}, {r.y})>"

def main():

    dot = Dot('dot-xml', 10, 6)
    circle = Circle('circle-xml', 6, 2, 3)  # Objetos de productos concretos
    rectangle = Rectangle('rectangle-xml', -5, 10, 5, 8)
    print(dot.draw(),'\n')

    xml_visitor = XMLExportVisitor()    
    json_visitor = JSONExportVisitor()  # Objetos de visitores concretos
    yaml_visitor = YAMLExportVisitor()

    print(xml_visitor.visit_dot(dot))
    print(json_visitor.visit_circle(circle))
    print(yaml_visitor.visit_rectangle(rectangle))

    '''
    Dot 'dot-xml' drew at coordinates -> (10, 6) 

    XML export done for: <dot-xml coordinates=(10, 6)>
    JSON export done for: <circle-xml radius=3 coordinates=(6, 2)>
    YAML export done for: <rectangle-xml width=5 height=8 coordinates=(-5, 10)>
    '''
if __name__ == '__main__':
    main()