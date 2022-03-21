from abc import ABC, abstractmethod
from figures import Triangle, Square, Pentagon


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
