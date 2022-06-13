from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def getType(self):
        pass


class Triangle(Polygon):
    def __init__(self):
        self.type = "Triangle"

    def getType(self):
        return self.type


class Square(Polygon):
    def __init__(self):
        self.type = "Square"

    def getType(self):
        return self.type


class Pentagon(Polygon):
    def __init__(self):
        self.type = "Pentagon"

    def getType(self):
        return self.type


class FigureCreator(ABC):
    @abstractmethod
    def createFigure(self):
        pass


class TriangleCreator(FigureCreator):
    def createFigure(self):
        return Triangle()


class SquareCreator(FigureCreator):
    def createFigure(self):
        return Square()


class PentagonCreator(FigureCreator):
    def createFigure(self):
        return Pentagon()

#Los creadores concretos sobre escriben la clase FigureCreator 
#de modo que devuelva un tipo diferente de figura

#La clase creadora declara el metodo Creator que devuelve nuevos objetos de figuras.