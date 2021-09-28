import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
        
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    def test_multiplica_dos_numeros(self):
        calc = Calculator(42, 2)
        self.assertEqual(84, calc.multiplicacion())
    
    def test_divide_dos_numeros(self):
        calc = Calculator(18, 3)
        self.assertEqual(6, calc.division())

    def test_potencia_de_un_numero(self):
        calc = Calculator(3, 3)
        self.assertEqual(27, calc.potencia())

    def test_raiz_de_un_numero(self):
        calc = Calculator(216, 3)
        self.assertEqual(6, calc.raiz())

    def test_dividir_entre_cero(self):
        calc = Calculator(25, 0)
        self.assertEqual(0, calc.division())

    def test_dividir_entre_cero_2(self):
        calc = Calculator(0, 25)
        self.assertEqual(0, calc.division()) 

    def test_raiz_num_negativo(self):
        calc = Calculator(-8,2)
        self.assertEqual(0, calc.raiz())

if __name__ == "__main__":
    unittest.main()