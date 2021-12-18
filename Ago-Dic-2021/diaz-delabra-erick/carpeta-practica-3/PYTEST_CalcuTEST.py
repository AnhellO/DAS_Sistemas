import pytest 
from PYTEST_Calcu import Calculator

'''PARTE 3 OPCIONAL: PYTEST'''

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (1,1,2),
        (100,50,150),
        (8,14,22)
    ]
)
def test_suma_dos_numeros(input_a, input_b, expected):
    assert Calculator.suma(input_a, input_b) == expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (4,2,2),
        (100,50,50),
        (15,8,7)
    ]
)
def test_resta_dos_numeros(input_a, input_b, expected):
    assert Calculator.resta(input_a, input_b) == expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (4,2,8),
        (100,3,300),
        (25,5,125)
    ]
)
def test_multiplicacion_dos_numeros(input_a, input_b, expected):
    assert Calculator.multiplicacion(input_a, input_b) == expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (4,2,2),
        (10,1,10),
        (2,0,"No se puede dividir entre 0")
    ]
)
def test_division_dos_numeros(input_a, input_b, expected):
    assert Calculator.division(input_a, input_b) == expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (81,2,9),
        (9,2,3),
        (-9,3,"No se puede raiz de negativos")
    ]
)
def test_division_dos_numeros(input_a, input_b, expected):
    assert Calculator.raizNumero(input_a, input_b) == expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2,2,4),
        (4,4,256),
        (3,5,243)
    ]
)
def test_potencia_de_numero(input_a, input_b, expected):
    assert Calculator.potencia(input_a, input_b) == expected