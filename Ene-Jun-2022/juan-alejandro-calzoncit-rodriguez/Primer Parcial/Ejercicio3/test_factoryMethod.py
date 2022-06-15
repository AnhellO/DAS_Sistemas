import unittest
from factoryMethod import *

'''
Suite de pruebas unitarias para las clases de factoryMethod.py
'''

class TestFactoryMethod(unittest.TestCase):
    def test_create_PolygonFactory(self):
        pf = PolygonFactory()

        self.assertIsInstance(pf , PolygonFactory)        

    def test_create_Triangle(self):
        triangle = Triangle()

        self.assertIsInstance(triangle, Triangle)
        self.assertIsInstance(triangle, Interface_Polygon)
        self.assertEqual(triangle.getType(),"It's a triangle")

    def test_create_Square(self):
        square = Square()

        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Interface_Polygon)
        self.assertEqual(square.getType(), "It's a square")

    def test_create_Pentagon(self):
        pentagon = Pentagon()

        self.assertIsInstance(pentagon, Pentagon)
        self.assertIsInstance(pentagon, Interface_Polygon)
        self.assertEqual(pentagon.getType(), "It's a pentagon")

    def test_PolygonFactory_Triangle(self):
        pf = PolygonFactory()
        triangle = Triangle()

        self.assertEqual(pf.getPolygon(triangle), "It's a triangle")

    def test_Polygon_Square(self):
        pf = PolygonFactory()
        square = Square()

        self.assertEqual(pf.getPolygon(square), "It's a square")

    def test_Polygon_Pentagon(self):
        pf = PolygonFactory()
        pentagon = Pentagon()

        self.assertEqual(pf.getPolygon(pentagon), "It's a pentagon")

if __name__ == '__main__':
    unittest.main()