import unittest

from calculadora import *

class CalculadoraTest(unittest.TestCase):
    def test_suma(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
    
    def test_resta(self):
        calc = Calculator(18, 7)
        self.assertEqual(11, calc.resta())

if __name__ == '__main__':
    unittest.main()