from figures_manager import PolygonFactory
from figures_creator import TriangleCreator, SquareCreator, PentagonCreator

if __name__ == '__main__':
    # Creatig a triangle figure using PolygonFactory
    polygon = PolygonFactory(TriangleCreator())
    triangle = polygon.getPolygon()

    # Creatig a Square figure using PolygonFactory
    polygon = PolygonFactory(SquareCreator())
    square = polygon.getPolygon()

    # Creatig a pentagon figure using PolygonFactory
    polygon = PolygonFactory(PentagonCreator())
    pentagon = polygon.getPolygon()

    figures = [triangle, square, pentagon]
    print("\tFigures: ")
    for figure in figures:
        print("* " + figure.getType())
