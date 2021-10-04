  
import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    #suma
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
    
    def test_suma_dos_numeros_negativos(self):
        calc = Calculator(-5, -10)
        self.assertEqual(-15, calc.suma())
    
    def test_suma_dos_numeros_negativo_positivo(self):
        calc = Calculator(5, -10)
        self.assertEqual(-5, calc.suma())
    #resta    
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())
   
    def test_resta_dos_numeros_negativos(self):
        calc = Calculator(-19, -8)
        self.assertEqual(-27, calc.suma())
    
    def test_resta_dos_numeros_negativo_positivo(self):
        calc = Calculator(19, -8)
        self.assertEqual(11, calc.suma())

    #multipliciono 
    def test_multiplicacion_dos_numeros_positivos(self):
        calc = Calculator(2, 2)
        self.assertEqual(4, calc.Multiplicion())
    
    def test_multiplicacion_dos_numeros_negativos(self):
        calc = Calculator(-2, -2)
        self.assertEqual(4, calc.Multiplicion())
    
    def test_multiplicacion_dos_numeros_negativo_psotivo(self):
        calc = Calculator(-2, 2)
        self.assertEqual(-4, calc.Multiplicion())
    
    #divicion
    def test_divicion_dos_numeros_poitivo(self):
        calc = Calculator(2, 2)
        self.assertEqual(1, calc.Division())
    
    def test_divicion_dos_numeros_negativo(self):
        calc = Calculator(-2, -2)
        self.assertEqual(1, calc.Division())
    
    def test_divicion_dos_numeros_uno_y_uno(self):
        calc = Calculator(2, -2)
        self.assertEqual(-1, calc.Division())
    
    def test_divicion_dos_numeros_cero(self):
        calc = Calculator(2, 0)
        self.assertEqual("indefinido", calc.Division())
    #potencia
    def test_potencia_dos_numeros(self):
        calc = Calculator(2, 2)
        self.assertEqual(4, calc.potencia())
    def test_potencia_dos_numeros_negativo(self):
        calc = Calculator(2, -2)
        self.assertEqual(.25, calc.potencia())
    #raiz
    def test_raiz_dos_numeros_raiz_positiva_par(self):
        calc = Calculator(4, 2)
        self.assertEqual(2, calc.raiz())
    
    def test_raiz_dos_numeros_raiz_negativa_par(self):
        calc = Calculator(-4, 2)
        self.assertEqual("numero imaginario", calc.raiz())
    
    def test_raiz_dos_numeros_raiz_positiva_inpar(self):
        calc = Calculator(8, 3)
        self.assertEqual(2, calc.raiz())
    
    def test_raiz_dos_numeros_raiz_positiva_inpar_negativa(self):
        calc = Calculator(8, -3)
        self.assertEqual(.5, calc.raiz())
    
    def test_raiz_dos_numeros_raiz_negativa_inpar(self):
        calc = Calculator(-8, 3)
        self.assertEqual(-2, calc.raiz())
    
    def test_raiz_dos_numeros_raiz_negativa_inpar(self):
        calc = Calculator(8, 0)
        self.assertEqual("indefinido", calc.raiz())

if __name__ == "__main__":
    unittest.main()