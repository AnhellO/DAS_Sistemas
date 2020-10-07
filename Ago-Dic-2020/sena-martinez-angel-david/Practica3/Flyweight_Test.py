import unittest
from Flyweight import *

class TargetTest(unittest.TestCase):
    def test_car(self):
        car = CarFamilies("audi",12345)
        self.assertEqual(CarFamilies(car)),("Objetivo: comportamiento del objetivo predeterminado")

if __name__ == "__main__":
    unittest.main() 