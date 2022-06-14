from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def num_of_sides(self):
        pass

class triangle(Polygon):
    def num_of_sides(self):
        return "3 sides"

class square(Polygon):
    def num_of_sides(self):
        return "4 sides"

class pentagonus(Polygon):
    def num_of_sides(self):
        return "5 sides"

class hexagone(Polygon):
    def num_of_sides(self):
        return "6 sides"

if __name__ == "__main__":
    tri = triangle()
    print(f"the triangle has {tri.num_of_sides()}")

    squ = square()
    print(f"the square has {squ.num_of_sides()}")

    pent = pentagonus()
    print(f"the pentagonus has {pent.num_of_sides()}")

    hex = hexagone()
    print(f"the hexagone has {hex.num_of_sides()}")