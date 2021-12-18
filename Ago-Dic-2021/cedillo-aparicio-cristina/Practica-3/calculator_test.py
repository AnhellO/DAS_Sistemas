import unittest
from unittest.case import TestCase

from calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())

    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    def test_multiplicacion_dos_numeros(self):
        calc = Calculator(10,8)
        self.assertEqual(80,calc.multiplicacion())

    def test_division_dos_numeros(self):
        calc = Calculator(4,16)
        self.assertEqual(0.25,calc.division())

    def test_division_entre_cero(self):
        calc = Calculator(2,0)
        self.assertEqual("No se puede dividir entre cero",calc.division())

    def test_potencia(self):
        calc = Calculator(2,2)
        self.assertEqual(4,calc.potencia())
    
    def test_raiz(self):
        calc = Calculator(4,12)
        self.assertEqual(24,calc.raiz())

    def test_raiz_cero(self):
        calc = Calculator(-4,12)
        self.assertEqual("No se aceptan números negativos para la raíz cuadrada", calc.raiz())


if __name__ == "__main__":
    unittest.main()
