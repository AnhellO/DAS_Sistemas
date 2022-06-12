import pytest
from figures import TriangleCreator, SquareCreator, PentagonCreator
from figures import Polygon, Triangle, Square, Pentagon
from figures import FigureCreator
from polygon_factory import PolygonFactory


class TestFactoryMethod:
    def test_creators(self):
        triangle = TriangleCreator()
        assert isinstance(triangle, FigureCreator)
        square = TriangleCreator()
        assert isinstance(square, FigureCreator)
        pentagon = TriangleCreator()
        assert isinstance(pentagon, FigureCreator)

    def test_figure_type(self):
        polygon = PolygonFactory((TriangleCreator()))
        triangle = polygon.getPolygon()
        assert triangle.getType() == 'Triangle'
        polygon = PolygonFactory((SquareCreator()))
        square = polygon.getPolygon()
        assert square.getType() == 'Square'
        polygon = PolygonFactory((PentagonCreator()))
        pentagon = polygon.getPolygon()
        assert pentagon.getType() == 'Pentagon'

    def test_instances(self):
        polygon = PolygonFactory((TriangleCreator()))
        triangle = polygon.getPolygon()
        assert isinstance(triangle, Triangle)
        assert isinstance(triangle, Polygon)

        polygon = PolygonFactory((SquareCreator()))
        square = polygon.getPolygon()
        assert isinstance(square, Square)
        assert isinstance(square, Polygon)

        polygon = PolygonFactory((PentagonCreator()))
        pentagon = polygon.getPolygon()
        assert isinstance(pentagon, Pentagon)
        assert isinstance(pentagon, Polygon)


if __name__ == '__main__':
    pytest.main()
