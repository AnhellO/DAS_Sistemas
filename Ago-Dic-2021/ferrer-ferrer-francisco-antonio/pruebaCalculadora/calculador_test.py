import unittest

from calculator import *
        ####py -m pytest pruebaCalculadora/calculador_test.py
class CalculatorTest(unittest.TestCase):

    def test_suma_dos_numeros(self):
        calc = calculator(5,10)
        self.assertEqual(15, calc.Suma())

    def test_resta_dos_numeros(self):
        calc = calculator(19,8)
        self.assertEqual(11, calc.Resta())

    def test_raiz_de_numero_negativo(self):
        calc = calculator(-4, 2)
        self.assertEqual(None, calc.Raiz())

    def test_dividir_entre_cero(self):
        calc = calculator(10,0)
        self.assertEqual(0, calc.Division())
    
   

if __name__ == "__main__":
    unittest.main()