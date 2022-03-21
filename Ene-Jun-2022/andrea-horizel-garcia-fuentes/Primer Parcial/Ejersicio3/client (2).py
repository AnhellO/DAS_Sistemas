from polygon_factory import PolygonFactory
from figures import TriangleCreator, SquareCreator, PentagonCreator

if __name__ == '__main__':
    triangle_creator = TriangleCreator()
    polygon = PolygonFactory(triangle_creator)
    triangle = polygon.getPolygon()
    print("Figure type: " + triangle.getType())

    square_creator = SquareCreator()
    polygon = PolygonFactory(square_creator)
    square = polygon.getPolygon()
    print("Figure type: " + square.getType())

    pentagon_creator = PentagonCreator()
    polygon = PolygonFactory(pentagon_creator)
    pentagon = polygon.getPolygon()
    print("Figure type: " + pentagon.getType())

    #
