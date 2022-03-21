from abc import ABC, abstractmethod
class Shape (ABC):
    @abstractmethod
    def move(self,x,y):
        self.x=x
        self.y=y
    @abstractmethod
    def draw(self):
       pass
    @abstractmethod
    def accept(v:Visitor):
        pass
class Dot(Shape):
    def __init__(self,id,x,y) -> None:
        self.id=id
        self.x=x
        self.y=y
    def move(self, x,y):
        return super().move(x, y)
    def draw(self):
         return "Dot "+ self.id +" drew at coordinates ->"+"("+ str(self.x) + ", "+ str(self.y) +")"
    
    def accept(self,v: Visitor):
        v.visit_dot(self)
class Circle (Shape):
    def __init__(self,id,x,y,radius) :
        self.id=id
        self.x=x
        self.y=y
        self.radius=radius
    def move(self, x,y):
        return super().move(x, y)
    def draw(self):
        return "Circle "+ self.id +" drew at coordinates ->"+"("+ str(self.x) + ", "+ str(self.y) +")"
    def accept(v: Visitor):
        v.visit_circle()
class Rectangle(Shape):
    def __init__(self,id,x,y,width,height) -> None:
        self.id=id
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def move(self, x,y):
        return super().move(x, y)
    def draw(self):
        return "Rectangle "+ self.id +" drew at coordinates ->"+"("+ str(self.x) + ", "+ str(self.y) +")"

    def accept(v: Visitor):
        v.visit_rectangle()
class CompoundShape (Shape):
    def accept(v: Visitor):
        v.visitCompoundShape()

class Visitor (ABC):
    @abstractmethod
    def visit_dot(self,d: Dot):
        pass
    @abstractmethod
    def visit_circle(self,c:Circle):
        pass
    @abstractmethod
    def visit_rectangle(self,r:Rectangle):
        pass
    @abstractmethod
    def visitCompoundShape(self,cs:CompoundShape):
        pass

class XMLExportVisitor (Visitor):
    def visit_dot(self, d: Dot):
       
        return super().visit_dot(d)
    def visit_circle(c: Circle):
        return super().visit_circle()
    def visit_rectangle(r: Rectangle):
        return super().visit_rectangle()
    def visitCompoundShape(cs: CompoundShape):
        return super().visitCompoundShape()

class YAMLExportVisitor (Visitor):
    def visit_dot(d: Dot):
        return super().visit_dot()
    def visit_circle(c: Circle):
        return super().visit_circle()
    def visit_rectangle(r: Rectangle):
        return super().visit_rectangle()
    def visitCompoundShape(cs: CompoundShape):
        return super().visitCompoundShape()

class JSONExportVisitor(Visitor):
    def visit_dot(d: Dot):
        return super().visit_dot()
    def visit_circle(c: Circle):
        return super().visit_circle()
    def visit_rectangle(r: Rectangle):
        return super().visit_rectangle()
    def visitCompoundShape(cs: CompoundShape):
        return super().visitCompoundShape()

class Application ():
    def export():
        exportVisitor= XMLExportVisitor()
        exportVisitor1= JSONExportVisitor()
        exportVisitor2=YAMLExportVisitor()
