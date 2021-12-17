import pytest
from calculator2 import *
######################SUMA####################
@pytest.mark.parametrize(
    "a, b, resultado", [(5, 5, 10),(8,4,12)])

def test_suma(a, b, resultado):
    assert Calculator.suma(a, b) == resultado
#####################RESTA##################################
@pytest.mark.parametrize(
    "a, b, resultado", [(5, 5, 0),(8,4,4)])

def test_resta(a, b, resultado):
    assert Calculator.resta(a, b) == resultado
#####################MULTIPLICACIÓN############################
@pytest.mark.parametrize(
    "a, b, resultado", [(5, 5, 25),(8,4,32)])

def test_multiplicacion(a, b, resultado):
    assert Calculator.multiplicacion(a, b) == resultado
########################DIVISIÓN##################################
@pytest.mark.parametrize(
    "a, b, resultado", [(5, 0, "No se puede dividir entre cero"),(64,8,8)])

def test_division(a, b, resultado):
    assert Calculator.division(a, b) == resultado
################################POTENCIA##################################3
@pytest.mark.parametrize(
    "a, b, resultado", [(4,8,65536),(2,8,256)])

def test_potencia(a, b, resultado):
    assert Calculator.potencia(a, b) == resultado
###########################RAÍZ########################################
@pytest.mark.parametrize(
    "a, b, resultado", [(4,5,10),(8,10,28.284271247461902),(9,10,30),(-4,12,"No se aceptan numeros negativos para la raiz cuadrada")])

def test_raiz(a, b, resultado):
    assert Calculator.raiz(a, b) == resultado

