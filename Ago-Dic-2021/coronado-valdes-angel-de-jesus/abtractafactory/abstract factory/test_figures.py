import pytest
from figures import *

class TestCalculatorPytest:
    #NO se puede instanciar una clase abtracta
    """def test_Figures(self):
        figures = Figures()
        assert figures.area()
        assert figures.perimeter()
    """

    def test_rectangle(self):
        rectangle = Retangle()
        assert rectangle.area()
        assert rectangle.perimeter()

    def test_cycle(self):
        cycle = Cycle()
        assert cycle.area()
        assert cycle.perimeter()

#*********** [ test of area (rectangle , cycle) ] ****************
    def test_area_rectangle(self):
        area_rectangle = TotalAreaRetangle()
        assert 9 == area_rectangle.FuctionArea([3,3])

    def test_area_cycle(self):
        area_cycle = TotalAreaCycle()
        assert 28.274333882308138 == area_cycle.FuctionArea([3])


#*********** [ test of perimeter (rectangle , cycle) ] ****************
    def test_perimeter_rectangle(self):
        perimeter_rectangle = TotalPerimeterRetangle()
        assert 18 == perimeter_rectangle.FuctionPerimeter([3,3])

    def test_perimeter_cycle(self):
        perimeter_cycle = TotalPerimeterCycle()
        assert 18.84955592153876 == perimeter_cycle.FuctionPerimeter([3])
"""
#*********** [ cliente ] ****************
    def test_client(self):
        client = Client()
        rectangle = Retangle()
        assert client.ClientCode(rectangle)
"""








