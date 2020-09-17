import unittest
from practicabridge import suma
from practicabridge import resta
from practicabridge import division
from practicabridge import multiplicacion

class BridgeMetodosTest(unittest.TestCase):
    def setUp(self):
        self.testcasessuma = (
            (5, 24, 29),
            (6, 7, 13),
            (0, 5, 5),
            (-6, -2, -8),
            (-7, 5, -2),
        )

        self.testcasesresta = (
            (5, 4, 1),
            (7, 3, 4),
            (-8, -2, -6),
            (-8, 5, -13),
            (-6, -7, 1),
        )

        self.testcasesmultiplicacion = (
            (5, 4, 20),
            (6, 7, 42),
            (-5, 4, -20),
            (-4, -2, 8),
            (-3, -2, 6),
        )

        self.testcasesdivision = (
            (6, 3, 2),
            (8, 2, 4),
            (-9, 3, -3),
            (-9, -9, 1),
            (-18, 4, -4.5),
        )

        self.suma = suma()
        self.resta = resta()
        self.division = division()
        self.multiplicacion = multiplicacion()
    
    def test_suma(self):
        for tc in self.testcasessuma:
            salida_real = self.suma.operation_imp(tc[0], tc[1])
            self.assertEqual(salida_real, "Suma de {} y {} = {}".format(tc[0], tc[1], tc[2]))

    def test_resta(self):
        for tc in self.testcasesresta:
            salida_real = self.resta.operation_imp(tc[0], tc[1])
            self.assertEqual(salida_real, "Resta de {} y {} = {}".format(tc[0], tc[1], tc[2]))

    def test_multiplicacion(self):
        for tc in self.testcasesmultiplicacion:
            salida_real = self.multiplicacion.operation_imp(tc[0], tc[1])
            self.assertEqual(salida_real, "Multiplicación de {} y {} = {}".format(tc[0], tc[1], tc[2]))
    
    def test_division(self):
        for tc in self.testcasesdivision:
            salida_real = self.division.operation_imp(float(tc[0]), float(tc[1]))
            self.assertEqual(salida_real, "División de {} y {} = {}".format(float(tc[0]), float(tc[1]), float(tc[2])))

if __name__ == '__main__':
    unittest.main()