import pytest
from calculator import Calculator

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [(2,3,5),
    (10,-2,8),
    (1/2,1/2,1)
    ]
)

def test_multiples_sumas(input_a,input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.suma() == expected


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (5,2,3),
        (-2,-2,0),
        (-4,2,-6)
    ]
)
def test_multiples_restas(input_a, input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.resta() == expected

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (5,2,10),
        (-2,-2,4),
        (-4,2,-8)
    ]
)
def test_multriplicacion(input_a, input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.multriplicacion() == expected


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (10,2,5),
        (-2,-2,1),
        (-4,2,-2),
        (10,0,'el diviendo no debe ser 0')
    ]
)
def test_divicion(input_a, input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.divicion() == expected


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (5,2,25),
        (-2,-2,0.25),
        (-4,2,16)
    ]
)
def test_potencia(input_a, input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.potencia() == expected

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (25,2,5),
        (2,25,1.0281138266560665),
        (30,2,5.477225575051661),
        (-2,5,'no se puede sacar la raiz negativa')

    ]
)
def test_raiz(input_a, input_b,expected):
    calc = Calculator(input_a,input_b)
    assert calc.raiz() == expected

