from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def numberOfSides(self):
        pass


class Triangle(Polygon):
    def __init__(self):
        self._type = __class__.__name__
        self._number_of_sides = 3

    def getType(self):
        return self._type

    def numberOfSides(self):
        return self._number_of_sides


class Square(Polygon):
    def __init__(self):
        self._type = __class__.__name__
        self._number_of_sides = 4

    def getType(self):
        return self._type

    def numberOfSides(self):
        return self._number_of_sides


class Pentagon(Polygon):
    def __init__(self):
        self._type = __class__.__name__
        self._number_of_sides = 5

    def getType(self):
        return self._type

    def numberOfSides(self):
        return self._number_of_sides
