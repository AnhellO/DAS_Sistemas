import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
        
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    '''PARTE 1: AGREGAR'''
    
    def test_multi_dos_numeros(self):
        calc = Calculator(5,5)
        self.assertEqual(25, calc.multiplicacion())

    def test_divi_dos_numeros(self):
        calc = Calculator(100, 2)
        self.assertEqual(50, calc.division())

    def test_raiz_numero(self):
        calc = Calculator(81, 2)
        self.assertEqual(9, calc.raizNumero())

    def test_potencia_numero(self):
        calc = Calculator(2, 2)
        self.assertEqual(4, calc.potencia())

    '''PARTE 2: CASOS ESPECIALES'''

    def test_ERROR_DIVISION_0(self):
        calc = Calculator(100, 0)
        self.assertEqual("No se puede dividir entre 0", calc.division())

    def test_ERROR_RAIZ_NEGATIVA(self):
        calc = Calculator(-9, 3)
        self.assertEqual("No se puede raiz de negativos", calc.raizNumero())
        

if __name__ == "__main__":
    unittest.main()