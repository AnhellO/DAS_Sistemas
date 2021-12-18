import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):

    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())

    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    def test_multriplicacion(self):
        calc = Calculator(5,2)
        self.assertEqual(10,calc.multriplicacion())

    def test_divicion(self):
        calc= Calculator(25,5)
        self.assertEqual(5,calc.divicion())

    def test_divicion_entre_0(self):
        calc= Calculator(25,0)
        self.assertEqual('el diviendo no debe ser 0',calc.divicion())

    def test_potencia_un_numero(self):
        calc = Calculator(5,2)
        self.assertEqual(25,calc.potencia())

    def test_raiz_un_numero(self):
        calc = Calculator(25,5)
        self.assertEqual(1.9036539387158786,calc.raiz())

    def test_raiz_negativa(self):
        calc = Calculator(-25,5)
        self.assertEqual('no se puede sacar la raiz negativa',calc.raiz())

if __name__ == "__main__":
    unittest.main()