from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass


class Triangle(Polygon):
    def __init__(self):
        self._sides = 3

    def num_of_sides(self):
        return self._sides

    def __str__(self):
        return f"The Triangle has {self._sides} sides."


class Square(Polygon):
    def __init__(self):
        self._sides = 4

    def num_of_sides(self):
        return self._sides

    def __str__(self):
        return f"The Square has {self._sides} sides."


class Pentagon(Polygon):
    def __init__(self):
        self._sides = 5

    def num_of_sides(self):
        return self._sides

    def __str__(self):
        return f"The Pentagon has {self._sides} sides."


class Hexagon(Polygon):
    def __init__(self):
        self._sides = 6

    def num_of_sides(self):
        return self._sides

    def __str__(self):
        return f"The Hexagon has {self._sides} sides."


if __name__ == '__main__':
    polygons = []

    polygons.append(Triangle())
    polygons.append(Square())
    polygons.append(Pentagon())
    polygons.append(Hexagon())

    for polygon in polygons:
        print(polygon)
