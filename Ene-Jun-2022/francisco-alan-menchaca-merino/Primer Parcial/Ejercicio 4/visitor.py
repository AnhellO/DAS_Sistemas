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
        msg = f"Dot '{self.id}' drew at "
        msg += f"coordinates -> ({self.x}, {self.y})"
        return msg

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
        msg = f"Circle '{self.id}' drew at "
        msg += f"coordinates -> ({self.x}, {self.y})"
        return msg

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
        msg = f"Rectangle '{self.id}' drew at "
        msg += f"coordinates -> ({self.x}, {self.y})"
        return msg

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
        msg = f"XML export done for: <dot-xml "
        msg += f"coordinates=({dot.x}, {dot.y})>"
        return msg

    def visit_circle(self, circle):
        msg = f"XML export done for: <circle-xml "
        msg += f"radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
        return msg

    def visit_rectangle(self, rectangle):
        msg = f"XML export done for: <rectangle-xml width={rectangle.width} "
        msg += f"height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"
        return msg


class JSONExportVisitor(Visitor):
    def visit_dot(self, dot):
        msg = f"JSON export done for: <dot-json "
        msg += f"coordinates=({dot.x}, {dot.y})>"
        return msg

    def visit_circle(self, circle):
        msg = f"JSON export done for: <circle-json "
        msg += f"radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
        return msg

    def visit_rectangle(self, rectangle):
        msg = f"JSON export done for: <rectangle-json width={rectangle.width} "
        msg += f"height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"
        return msg


class YAMLExportVisitor(Visitor):
    def visit_dot(self, dot):
        msg = f"YAML export done for: <dot-yaml "
        msg += f"coordinates=({dot.x}, {dot.y})>"
        return msg

    def visit_circle(self, circle):
        msg = f"YAML export done for: <circle-yaml "
        msg += f"radius={circle.radius} coordinates=({circle.x}, {circle.y})>"
        return msg

    def visit_rectangle(self, rectangle):
        msg = f"YAML export done for: <rectangle-yaml width={rectangle.width} "
        msg += f"height={rectangle.height} coordinates=({rectangle.x}, {rectangle.y})>"
        return msg
