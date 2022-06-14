import string
from visitor_interfaces import Shape,Visitor

#Clase Dot que pedia el test_dot
class Dot(Shape):
    #Constructor el cual requiere como parametros un id de tipo string, y dos puntos los cuales son enteros de acuerdo al test
    def __init__(self, id = string, x = int, y = int):
        self.id = id
        self.x = x
        self.y = y
    #Metodo move el cual recibe 2 variables y mueve el punto de donde esta a los valores indicados
    def move(self,x,y):
        self.x = x
        self.y = y
    #metodo draw, el cual te muestra en donde se encuentra el punto actualmente
    def draw(self):
        return "Dot '{id}' drew at coordinates -> ({x}, {y})".format(id = self.id, x = self.x, y = self.y)
    #metodo accept, el cual hace que herede de si mismo como de Visitor e indica con que objeto se trabajara
    def accept(self, v: Visitor):
        v.visitDot(self)

class Circle(Shape):
    
    def __init__(self, id = string, x = int, y = int, radius = float):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
    #Metodo move el cual recibe 2 variables y mueve el circulo a donde se ha indicado
    def move(self,x,y):
        self.x = x
        self.y = y
    #Metodo draw el cual retorna un string mostrando donde se ha dibujado el circulo que se ha creado
    def draw(self):
        return "Circle '{id}' drew at coordinates -> ({x}, {y})".format(id = self.id, x = self.x, y = self.y)
    #Metodo accept, el cual hereda de visitor como de si mismo e indica con que objeto se trabajara
    def accept(self, v: Visitor):
        v.visitCircle(self)

class Rectangle(Shape):
    #Constructor el cual recibe el id, variables x y y de tipo enteros, y width, height tipo flotante en caso de ser necesario
    def __init__(self, id = string, x = int, y = int, width = float, height = float):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    #Metodo move el cual recive 2 variables para mover el rectangulo de lugar
    def move(self,x,y):
        self.x = x
        self.y = y
    #Metodo draw el cual retorna un string mostrando el rectangulo y el lugar donde se encuentra
    def draw(self):
        return "Rectangle '{id}' drew at coordinates -> ({x}, {y})".format(id = self.id, x = self.x, y = self.y)
    #Metodo accept el cual hereda de visitor como de Rectangle y nos indica el objeto con el que se trabajara
    def accept(self, v: Visitor):
        v.visitCircle(self)

#Clases exportadoras que implementan la interfaz de Visitor
#Cada clase contiene 3 metodos, un metodo para visitar cada figura en especifico y retornar un string 
#el cual muestra que la exportacion fue terminada, cada metodo recibe la figura correspondiente al nombre del metodo
class XMLExportVisitor(Visitor):
    
    def visit_dot(self, dot = Dot):
        return "XML export done for: <{id} coordinates=({x}, {y})>".format(id = dot.id, x = dot.x, y = dot.y)
    def visit_circle(self, circle = Circle):
        return "XML export done for: <{id} radius={radius} coordinates=({x}, {y})>".format(id = circle.id,
         radius = circle.radius, x = circle.x, y = circle.y)
    def visit_rectangle(self, rectangle = Rectangle):
        return "XML export done for: <{id} width={width} height={height} coordinates=({x}, {y})>".format(id = rectangle.id,
         width = rectangle.width, height = rectangle.height, x = rectangle.x, y = rectangle.y)

class JSONExportVisitor(Visitor):
    
    def visit_dot(self, dot = Dot):
        return "JSON export done for: <{id} coordinates=({x}, {y})>".format(id = dot.id, x = dot.x, y = dot.y)
    def visit_circle(self, circle = Circle):
        return "JSON export done for: <{id} radius=3 coordinates=(6, 2)>".format(id = circle.id,
         radius = circle.radius, x = circle.x, y = circle.y)
    def visit_rectangle(self, rectangle = Rectangle):
        return "JSON export done for: <{id} width={width} height={height} coordinates=({x}, {y})>".format(id = rectangle.id,
         width = rectangle.width, height = rectangle.height, x = rectangle.x, y = rectangle.y)

class YAMLExportVisitor(Visitor):
    
    def visit_dot(self, dot = Dot):
        return "YAML export done for: <{id} coordinates=({x}, {y})>".format(id = dot.id, x = dot.x, y = dot.y)
    def visit_circle(self, circle = Circle):
        return "YAML export done for: <{id} radius={radius} coordinates=({x}, {y})>".format(id = circle.id,
         radius = circle.radius, x = circle.x, y = circle.y)
    def visit_rectangle(self, rectangle = Rectangle):
        return "YAML export done for: <{id} width={width} height={height} coordinates=({x}, {y})>".format(id = rectangle.id,
         width = rectangle.width, height = rectangle.height, x = rectangle.x, y = rectangle.y)



