import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    # Test de suma de numeros
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())

    # Tes de resta de numeros
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    # Test de multiplicacion de numeros
    def test_multiplicacion_dos_numeros(self):
        calc = Calculator(15, 10)
        self.assertEqual(150, calc.multiplicacion())

########################################## PARTE 2 #####################################################

    # Test de division de numeros
    def test_division_dos_numeros(self):
        calc = Calculator(10, 2)
        self.assertEqual(5, calc.division())

    # Tes de division de numeros
    def test_division_dos_numeros_cuando_b_es_cero(self):
        calc = Calculator(10, 0)
        self.assertEqual("No es posible dividir entre 0", calc.division())

    # Test de potencia de numeros
    def test_potencia_de_numeros(self):
        calc = Calculator(2, 5)
        self.assertEqual(32, calc.potencia())

        # Un numero elevado a la cero
        calc = Calculator(2, 0)
        self.assertEqual(1, calc.potencia())

    # Tets de raiz de numeros
    def test_raiz_de_numeros(self):
        calc = Calculator(25, 2)
        self.assertEqual(5, calc.raiz())

        # Una raiz negativa
        calc = Calculator(-5, 2)
        self.assertEqual("No se puede raiz negativa", calc.raiz())

        # Una raiz de cero
        calc = Calculator(0, 2)
        self.assertEqual(0, calc.raiz())

if __name__ == "__main__":
    unittest.main()