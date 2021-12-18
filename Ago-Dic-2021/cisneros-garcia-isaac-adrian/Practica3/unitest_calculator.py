import unittest
from calculator import *


class testsCalculator(unittest.TestCase):

    def testSumaDosNumeros(self):
        prueba = Calculator(100, 54)
        self.assertEqual(prueba.suma(), 154)

    def testSobreCero(self):
        prueba = Calculator(5, 0)
        self.assertEqual(prueba.division(),
                         'ZeroDivisionError: division by zero')

    def testRaizDeNegativo(self):
        prueba = Calculator(-5, 2)
        self.assertEqual(prueba.raiz(),
                         'Imposible Raiz de un Negativo')

    def testRaizCero(self):
        prueba = Calculator(100, 0)
        self.assertEqual(prueba.raiz(),
                         'Sin Definir')

    def testPotencia(self):
        prueba = Calculator(10, 2)
        self.assertEqual(prueba.potencia(), 100)

    def testPotenciaALaCero(self):
        prueba = Calculator(10, 0)
        self.assertEqual(prueba.potencia(), 1)

    def testRestaDosNumeros(self):
        prueba = Calculator(100, 52)
        self.assertEqual(prueba.resta(), 48)

    def testMultiplicacion(self):
        prueba = Calculator(100, 23)
        self.assertEqual(prueba.multiplicacion(), 2300)


if __name__ == "__main__":
    unittest.main()