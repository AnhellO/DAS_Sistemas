import unittest

from Calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
        
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    def test_multiplicacion_dos_numeros(self):
        calc = Calculator(5,5)
        self.assertEqual(25,calc.multiplicacion())
    
    def test_division(self):
        calc = Calculator(100,4)
        self.assertEqual(25,calc.division())
    
    def test_division_cero(self):
        calc = Calculator(30,0)
        self.assertEqual("Favor de hacer una operación valida, MATH ERROR",calc.division())
    
    def test_potencia(self):
        calc = Calculator(100,2)
        self.assertEqual(10000,calc.potencia())
    
    def test_raiz_cuadrada_positiva(self):
        calc = Calculator(9,2)
        self.assertEqual(3,calc.raiz())

    def test_raiz_cubica(self):
        calc = Calculator(27,3)
        self.assertEqual(3,calc.raiz())
    
    def test_raiz_Basepar_negativa(self):
        calc = Calculator(-5,2)
        self.assertEqual("Error!!!",calc.raiz())

    def test_raiz_baseImpar_negativa(self):
        calc = Calculator(-2,3)
        self.assertEqual(-1.2599210498948732,calc.raiz())
    
    def test_raiz_baseImpar_negativa2(self):
        calc = Calculator(-3,5)
        self.assertEqual(-1.2457309396155174,calc.raiz())

if __name__ == "__main__":
    unittest.main()