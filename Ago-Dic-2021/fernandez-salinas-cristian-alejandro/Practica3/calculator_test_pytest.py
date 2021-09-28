import pytest
from calculator import Calculator

def test_suma_dos_numeros():
    assert Calculator.suma(Calculator(13,2)) == 15
        
def test_resta_dos_numeros():
    assert Calculator.resta(Calculator(19,8)) == 11

def test_multiplica_dos_numeros():
    assert Calculator.multiplicacion(Calculator(42,2)) == 84
    
def test_divide_dos_numeros():
    assert Calculator.division(Calculator(18,3)) == 6

def test_potencia_de_un_numero():
    assert Calculator.potencia(Calculator(3,3)) == 27

def test_raiz_de_un_numero():
    assert Calculator.raiz(Calculator(216,3)) == 6

def test_dividir_entre_cero():
    assert Calculator.division(Calculator(25,0)) == 0

def test_dividir_entre_cero_2():
    assert Calculator.division(Calculator(0,25)) == 0

def test_raiz_num_negativo():
    assert Calculator.raiz(Calculator(-8,2)) == 0