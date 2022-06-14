import unittest
from factory import *

class factory_test(unittest.TestCase):
    def test_polygonFactory(self):
        triangulo = Triangle()
        cuadrado = Square()
        pentagono = Pentagon()
        self.assertEquals(triangulo, PolygonFactory(triangulo).getPolygon())
        self.assertEquals(cuadrado, PolygonFactory(cuadrado).getPolygon())
        self.assertEquals(pentagono, PolygonFactory(pentagono).getPolygon())
    def test_Triangle(self):
        triangulo = Triangle()
        self.assertEqual("El triangulo es un poligono con 3 lados", triangulo.getType())
    def test_Square(self):
        cuadrado = Square()
        self.assertEqual("El cuadrado es un poligono con 4 lados", cuadrado.getType())
    def test_Pentagon(self):
        pentagono = Pentagon()
        self.assertEqual("El pentagono es un poligono con 5 lados", pentagono.getType())

if __name__ == "__main__":
    unittest.main()