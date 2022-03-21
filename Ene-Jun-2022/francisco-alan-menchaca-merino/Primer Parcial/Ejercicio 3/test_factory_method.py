from figures_manager import PolygonFactory
from figures import Polygon, Triangle, Square, Pentagon
from figures_creator import TriangleCreator, SquareCreator, PentagonCreator
from figures_creator import FigureCreator
import pytest


class TestFactoryMethod:
    def test_figures_creator_instances(self):
        triangle_creator = TriangleCreator()
        square_creator = TriangleCreator()
        pentagon_creator = TriangleCreator()

        assert isinstance(triangle_creator, FigureCreator)
        assert isinstance(square_creator, FigureCreator)
        assert isinstance(pentagon_creator, FigureCreator)

    @pytest.fixture(autouse=True)
    def generate_polygon(self):
        polygon = PolygonFactory((TriangleCreator()))
        triangle = polygon.getPolygon()

        polygon = PolygonFactory((SquareCreator()))
        square = polygon.getPolygon()

        polygon = PolygonFactory((PentagonCreator()))
        pentagon = polygon.getPolygon()

        return (triangle, square, pentagon)

    def test_figures_instances(self, generate_polygon):
        triangle = generate_polygon[0]
        assert isinstance(triangle, Triangle)
        assert isinstance(triangle, Polygon)

        square = generate_polygon[1]
        assert isinstance(square, Square)
        assert isinstance(square, Polygon)

        pentagon = generate_polygon[2]
        assert isinstance(pentagon, Pentagon)
        assert isinstance(pentagon, Polygon)

    def test_get_type(self, generate_polygon):
        triangle = generate_polygon[0]
        assert triangle.getType() == 'Triangle'

        square = generate_polygon[1]
        assert square.getType() == 'Square'

        pentagon = generate_polygon[2]
        assert pentagon.getType() == 'Pentagon'

    def test_number_of_sides(self, generate_polygon):
        triangle = generate_polygon[0]
        assert triangle._number_of_sides == 3

        square = generate_polygon[1]
        assert square._number_of_sides == 4

        pentagon = generate_polygon[2]
        assert pentagon._number_of_sides == 5


if __name__ == '__main__':
    pytest.main()
