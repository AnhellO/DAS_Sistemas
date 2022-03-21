import unittest
from ejercicio_3 import *

class PolygonFactory_test(unittest.TestCase):
    
    def test_crear_objetos(self):

        triangle = Triangle()
        self.assertIsInstance(triangle, Triangle)

        square = Square()
        self.assertIsInstance(square, Square)
        
        pentagon = Pentagon()
        self.assertIsInstance(pentagon, Pentagon)

    def test_obtener_tipo(self):
        triangle = Triangle()
        self.assertEqual(triangle.getType(), "Triangle")

        square = Square()
        self.assertEqual(square.getType(), "Square")

        pentagon = Pentagon()
        self.assertEqual(pentagon.getType(), "Pentagon")


if __name__=="__main__":
    unittest.main()