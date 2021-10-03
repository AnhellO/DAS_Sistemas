import pytest
from calculator import *


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (-5, 2, 'Imposible Raiz de un Negativo')
])
def testRaizDeNegativo(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).raiz() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (5, 0, 'ZeroDivisionError: division by zero')
])
def testSobreCero(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).division() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (100, 54, 154)
])
def testSumaDosNumeros(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).suma() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (150, 75, 75)
])
def testRestaDosNumeros(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).resta() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (5, 2, 25)
])
def testPotencia(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).potencia() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (100, 0, 'Sin Definir')
])
def testRaizCero(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).raiz() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (10, 0, 1)
])
def testPotenciaALaCero(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).potencia() == expected_result


@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (100, 23, 2300)
])
def testMultiplicacion(input_a, input_b, expected_result):
    assert Calculator(input_a, input_b).multiplicacion() == expected_result
