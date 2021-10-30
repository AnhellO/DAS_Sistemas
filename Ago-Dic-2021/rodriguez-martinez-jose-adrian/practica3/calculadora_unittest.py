import unittest
from calculadora import Calculadora

class practica3(unittest.TestCase):

    def test_multiplicacion(self):
        calc = Calculadora(5, 10)
        resultado = calc.multiplicacion()
        salida_esperada = 50
        self.assertEqual(resultado, salida_esperada)

    def test_division(self):
        calc = Calculadora(50, 10)
        resultado = calc.division()
        salida_esperada = 5
        self.assertEqual(resultado, salida_esperada)

    def test_potencia(self):
        calc = Calculadora(5, 2)
        resultado = calc.potencia()
        salida_esperada = 25
        self.assertEqual(resultado, salida_esperada)

    def test_division_entre_cero(self):
        calc = Calculadora(25, 0)
        resultado = calc.division()
        salida_esperada = 'No se puede dividir entre cero'
        self.assertEqual(resultado, salida_esperada)


if __name__ == '__main__':
    unittest.main() 