import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
        
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())
    
    def test_multiplicación_dos_numeros(self):
        calc = Calculator(2,5)
        self.assertEqual(10,calc.multi())
    
    def test_divición_dos_numeros(self):
        calc = Calculator(0,10)
        self.assertEqual(0,calc.divicion())

    def test_potencia_dos_numeros(self):
        calc = Calculator(5,2)
        self.assertEqual(25,calc.potencia())
    
    def test_raiz_dos_numeros(self):
        calc = Calculator(-2,64)
        self.assertEqual(-99,calc.raiz())
    


if __name__ == "__main__":
    unittest.main()