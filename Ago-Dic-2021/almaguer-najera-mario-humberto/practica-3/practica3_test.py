import unittest
from calculator import Calculator

class practica3(unittest.TestCase):

    def test_multiplicacion(self):
        calc = Calculator(5, 3)
        resultado = calc.multiplicacion()
        salida_esperada = 15
        self.assertEqual(resultado, salida_esperada)

    def test_division(self):
        calc = Calculator(15, 3)
        resultado = calc.division()
        salida_esperada = 5
        self.assertEqual(resultado, salida_esperada)

    def test_potencia(self):
        calc = Calculator(10, 2)
        resultado = calc.potencia()
        salida_esperada = 100
        self.assertEqual(resultado, salida_esperada)

    def test_raiz(self):
        calc = Calculator(64, 2)
        resultado = calc.raiz()
        salida_esperada = 8
        self.assertEqual(resultado, salida_esperada)

    def test_division_entre_cero(self):
        calc = Calculator(25, 0)
        resultado = calc.division()
        salida_esperada = 'Error!, no se puede dividir entre cero o menor a cero.'
        self.assertEqual(resultado, salida_esperada)

    def test_raiz_de_numero_negativo(self):
        calc = Calculator(-64, 2)
        resultado = calc.raiz()
        salida_esperada = 'Error!, no se puede obtener la raiz de un numero negativo.'
        self.assertEqual(resultado, salida_esperada)

if __name__ == '__main__':
    unittest.main()