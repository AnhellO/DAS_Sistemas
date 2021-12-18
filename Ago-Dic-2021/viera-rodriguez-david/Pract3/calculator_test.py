import unittest
from calculator import *

class CalculatorTest(unittest.TestCase):

    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())
        
    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())
    
    def test_multiplicacion_dos_numeros(self):
        calc = Calculator(5, 9)
        self.assertEqual(45, calc.multiplicacion())
    
    def test_division_dos_numeros(self):
        test_case = [
            (25,5,5),
            #Division entre 0#
            (6,0,"Math ERROR"),
        ]
        for tc in test_case:
            calc = Calculator(tc[0], tc[1])
            self.assertEqual(tc[2], calc.division()) 
        
    def test_potencia_dos_numeros(self):
        calc = Calculator(2, 4)
        self.assertEqual(16, calc.potencia())
    
    def test_raiz_dos_numeros(self):
        test_case = [
            (8,3,2),
            #Raiz Negativa#
            (-1,2,"Math ERROR"),
        ]
        for tc in test_case:
            calc = Calculator(tc[0], tc[1])
            self.assertEqual(tc[2], calc.raiz())
    
if __name__ == "__main__":
    unittest.main()
