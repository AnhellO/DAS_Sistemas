import abc

class Shape(metaclass=abc.ABCMeta): #clase sharpe de ella herdan 
    @abc.abstractmethod
    def draw(self, color):
        pass

class Triangle(Shape):
    def draw(self, color):
        print("Drawing Triangle with color " + color)

class Circle(Shape):
    def draw(self, color):
        print("Drawing Circle with color " + color)

class Drawing(Shape):
    def __init__(self):
        self.shapes = []

    def draw(self, color):
        for sh in self.shapes:
            sh.draw(color)

    def add(self, sh):
        self.shapes.append(sh)

    def remove(self, sh):
        self.shapes.remove(sh)

    def clear(self):
        print("Clearing all the shapes from drawing")
        self.shapes = []

if __name__ == '__main__':
    tri1 = Triangle()
    tri2 = Triangle()
    cir  = Circle()

    drawing = Drawing()
    drawing.add(tri1)
    drawing.add(tri2)
    drawing.add(cir)

    drawing.draw("Red")

    drawing.clear()

    drawing.add(tri1)
    drawing.add(cir)
    drawing.draw("Green")
