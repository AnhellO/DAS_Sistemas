################################## PARTE 3 #################################

import pytest
from calculator_pytest import Calculator

#################################### Test de suma de numeros con pytest ###########################
@pytest.mark.parametrize(
    "a, b, resultado", [(5, 5, 10), (10, 100, 110)])

def test_suma_dos_numero(a, b, resultado):
    assert Calculator.suma(a, b) == resultado


###################################### Test de resta de numeros con pytest ##############################
@pytest.mark.parametrize(
    "a, b, resultado", [(8, 5, 3), (5, 8, -3)])

def test_resta_dos_numeros(a, b, resultado):
    assert Calculator.resta(a, b) == resultado


######################################### Test de multiplicacion de numeros con pytest #########################
@pytest.mark.parametrize(
    "a, b, resultado", [(8, 5, 40), (5, 0, 0)])

def test_multiplicacion_dos_numeros(a, b, resultado):
    assert Calculator.multiplicacion(a, b) == resultado


#################################### Test de division de numeros con pytest ######################################
@pytest.mark.parametrize(
    "a, b, resultado", [(10, 2, 5), (10, 0, "No es posible dividir entre 0")])

def test_division_dos_numeros(a, b, resultado):
    assert Calculator.division(a, b) == resultado


########################################### Test de potencia de numeros con pytest ######################################
@pytest.mark.parametrize(
    "a, b, resultado", [(10, 2, 100), (10, 0, 1)])

def test_potencia_de_numeros(a, b, resultado):
    assert Calculator.potencia(a, b) == resultado


############################################# Test de raiz de numeros con pytest ##########################################
@pytest.mark.parametrize(
    "a, b, resultado", [(64, 2, 8), (-1, 2, "No se puede raiz negativa"), (0, 2, 0)])

def test_raiz_de_numeros(a, b, resultado):
    assert Calculator.raiz(a, b) == resultado