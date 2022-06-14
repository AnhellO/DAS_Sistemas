from abc import ABC, abstractmethod

# interfaz


class Shape(ABC):

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def draw():
        pass

# elemento
class Dot(Shape):

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Dot '{self.id}' drew at coordinates -> ({self.x}, {self.y})"


class Circle(Shape):

    def __init__(self, id, x, y, radius):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x,y):
        self.x = x
        self.y = y

    def draw(self):
        return f"Circle '{self.id}' drew at coordinates -> ({self.x}, {self.y})"


class Rectangle(Shape):

    def __init__(self, id, x, y, width, height):
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


class XMLExportVisitor():

    def visit_dot(self,dot):
        dot = Dot(id,x,y)

    def visit_circle():
        circle = Circle

    def visit_rectangle():
        rectangle = Rectangle

class JSONExportVisitor():

    def visit_dot():
        dot = Dot

    def visit_circle():
        circle = Circle

    def visit_rectangle():
        rectangle = Rectangle

class YAMLExportVisitor():

    def visit_dot():
        dot = Dot

    def visit_circle():
        circle = Circle

    def visit_rectangle():
        rectangle = Rectangle