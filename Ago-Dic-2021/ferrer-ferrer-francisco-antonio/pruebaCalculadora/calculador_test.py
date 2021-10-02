import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = calculator(5, 10)
        self.assertEqual(15, calc.Suma())
    def test_resta_dos_numeros(self):
        calc = calculator(19,8)
        self.assertEqual(11, calc.Resta())