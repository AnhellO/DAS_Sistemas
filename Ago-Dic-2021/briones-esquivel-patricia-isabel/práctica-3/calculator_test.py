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
        calc = Calculator(5, 5)
        self.assertEqual(25, calc.multiplicacion())

    def test_divide_dos_numeros(self):
        # --test_cases[0],[1]: Entradas, --test_cases[2]: Salida esperada
        test_cases = [
            #Test case: División simple
            (10, 2, 5),
            #Test case: División entre 0
            (10, 0, 'error'),
            ]

        for tc in test_cases:
            calc = Calculator(tc[0], tc[1])
            self.assertEqual(tc[2], calc.division())

    def test_potencia_de_un_numero(self):
        # --test_cases[0],[1]: Entradas, --test_cases[2]: Salida esperada
        # [0] Número a potenciar, [1] Potencia, [2] resultado
        test_cases = [
            #Test case: Potencia simple
            (5, 2, 25),
            #Test case: Potencia negativa
            (5, -2, 0.04),
            ]

        for tc in test_cases:
            calc = Calculator(tc[0], tc[1])
            self.assertEqual(tc[2], calc.potencia())

    def test_raiz_de_un_numero(self):
        # --test_cases[0],[1]: Entradas, --test_cases[2]: Salida esperada
        # [0] Número a sacar raíz, [1] índice de raíz, [2] resultado
        test_cases = [
            #Test case: Raiz simple
            (25, 2, 5),
            #Test case: Raíz de un número negativo
            (-1, 2, 'error'),
            ]

        for tc in test_cases:
            calc = Calculator(tc[0], tc[1])
            self.assertEqual(tc[2], calc.raiz())

if __name__ == "__main__":
    unittest.main()
