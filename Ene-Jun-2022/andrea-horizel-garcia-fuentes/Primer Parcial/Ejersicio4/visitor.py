from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class Dot(Shape):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return "Dot '" + self.id + "' drew at coordinates -> (" + str(self.x) + ", " + str(self.y) + ")"

    def accept(self, visitor):
        return visitor.visit_dot(self)


class Circle(Shape):
    def __init__(self, id, x, y, radius):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return "Circle '" + self.id + "' drew at coordinates -> (" + str(self.x) + ", " + str(self.y) + ")"

    def accept(self, visitor):
        return visitor.visit_circle(self)


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
        return "Rectangle '" + self.id + "' drew at coordinates -> (" + str(self.x) + ", " + str(self.y) + ")"

    def accept(self, visitor):
        return visitor.visit_rectangle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot):
        pass

    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot):
        return "XML export done for: <dot-xml coordinates=(" + str(dot.x) + ", " + str(dot.y) + ")>"

    def visit_circle(self, circle):
        return "XML export done for: <circle-xml radius=" + str(circle.radius) + " coordinates=(" + str(circle.x) + ", " + str(circle.y) + ")>"

    def visit_rectangle(self, rectangle):
        return "XML export done for: <rectangle-xml width=" + str(rectangle.width) + " height=" + str(rectangle.height) + " coordinates=(" + str(rectangle.x) + ", " + str(rectangle.y) + ")>"


class JSONExportVisitor(Visitor):
    def visit_dot(self, dot):
        return "JSON export done for: <dot-json coordinates=(" + str(dot.x) + ", " + str(dot.y) + ")>"

    def visit_circle(self, circle):
        return "JSON export done for: <circle-json radius=" + str(circle.radius) + " coordinates=(" + str(circle.x) + ", " + str(circle.y) + ")>"

    def visit_rectangle(self, rectangle):
        return "JSON export done for: <rectangle-json width=" + str(rectangle.width) + " height=" + str(rectangle.height) + " coordinates=(" + str(rectangle.x) + ", " + str(rectangle.y) + ")>"


class YAMLExportVisitor(Visitor):
    def visit_dot(self, dot):
        return "YAML export done for: <dot-yaml coordinates=(" + str(dot.x) + ", " + str(dot.y) + ")>"

    def visit_circle(self, circle):
        return "YAML export done for: <circle-yaml radius=" + str(circle.radius) + " coordinates=(" + str(circle.x) + ", " + str(circle.y) + ")>"

    def visit_rectangle(self, rectangle):
        return "YAML export done for: <rectangle-yaml width=" + str(rectangle.width) + " height=" + str(rectangle.height) + " coordinates=(" + str(rectangle.x) + ", " + str(rectangle.y) + ")>"
