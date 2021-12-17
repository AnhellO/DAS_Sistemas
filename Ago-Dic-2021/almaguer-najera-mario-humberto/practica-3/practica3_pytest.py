import pytest
from calculator import Calculator

@pytest.mark.parametrize(
    "a,b,esperado",
    [(5, 5, 10),
    (1/2, 1/2, 1),
    (23, -2, 21)
    ]
)

def test_sumas(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.suma() == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [(10, 5, 5),
    (5/2, 1/2, 2),
    (-50, 5, -55)
    ]
)

def test_restas(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.resta() == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [(5, 5, 25),
    (2/4, 2, 1),
    (-5, 5, -25)
    ]
)

def test_multiplicaciones(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.multiplicacion() == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [(15, 3, 5),
    (25, 0, 'Error!, no se puede dividir entre cero o menor a cero.'),
    (1/2, 1/2, 1)
    ]
)

def test_divisiones(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.division() == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [(64, 2, 8),
    (-64, 2, 'Error!, no se puede obtener la raiz de un numero negativo.')
    ]
)

def test_raices(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.raiz() == esperado

@pytest.mark.parametrize(
    "a, b, esperado",
    [(2, 2, 4),
    (16, 2, 256),
    (8, 2, 64)
    ]
)

def test_potencias(a, b, esperado):
    calc = Calculator(a, b)
    assert calc.potencia() == esperado