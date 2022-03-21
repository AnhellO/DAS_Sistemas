from asyncio.windows_events import NULL
from distutils.log import error
from msilib.schema import Error
import unittest
from exam_parte_3 import *
class PolyTest(unittest.TestCase):
    def test_PolygonFactory(self):
         figura_1=PolygonFactory.getPolygon("T")
         self.assertEqual(figura_1().getType(),"triangulo")
         figura_2=PolygonFactory.getPolygon("C")
         self.assertEqual(figura_2().getType(),"cuadrado")
         figura_3=PolygonFactory.getPolygon("P")
         self.assertEqual(figura_3().getType(),"pentagono")


if __name__ == "__main__":
    
    unittest.main()