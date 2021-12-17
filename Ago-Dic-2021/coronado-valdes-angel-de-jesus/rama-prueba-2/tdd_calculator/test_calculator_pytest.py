import pytest
from calculator import *

class TestCalculatorPytest:
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        assert 15 == calc.suma()

    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        assert 11==calc.resta()
    
    def test_multiplicación_dos_numeros(self):
        calc = Calculator(2,5)
        assert 10==calc.multi()
    
    def test_divición_dos_numeros(self):
        calc = Calculator(0,10)
        assert 0==calc.divicion()

    def test_potencia_dos_numeros(self):
        calc = Calculator(5,2)
        assert 25==calc.potencia()
    
    def test_raiz_dos_numeros(self):
        calc = Calculator(-2,64)
        assert -99==calc.raiz()