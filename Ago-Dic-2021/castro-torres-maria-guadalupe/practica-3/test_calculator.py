import pytest

from calculator import *

@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (1, 2, 3),
        (2, 2, 4),
        (0, 0, 0)
    ]
)

def test_suma(a , b, resultado_esperado):
    assert Calculator.suma(a, b) == resultado_esperado


@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (2,1, 1),
        (-8, 2, -10),
        (-6, 2, -8)
    ]
)        
 
def test_resta(a , b, resultado_esperado):
    assert Calculator.resta(a, b) == resultado_esperado


@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (2,-1, -2),
        (2, -2, -4),
        (6, -2, -12)
    ]
)        
 
def test_multiplicacion(a , b, resultado_esperado):
    assert Calculator.multiplicacion(a, b) == resultado_esperado  


@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (0, 1, 0),
        (2, 1, 2),
        (6, 2, 3)
    ]
)        
 
def test_division(a , b, resultado_esperado):
    assert Calculator.division(a, b) == resultado_esperado


@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (2,0, "El divisor no puede ser cero"),
        (6,0, "El divisor no puede ser cero"),
        (5,0, "El divisor no puede ser cero")
    ]
)        
 
def test_division_entre_cero(a , b, resultado_esperado):
    assert Calculator.division(a, b) == resultado_esperado




@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (1, 1, 1),
        (2, 2, 4),
        (3, 2, 9)
    ]
)        
 
def test_potencia(a , b, resultado_esperado):
    assert Calculator.potencia(a, b) == resultado_esperado    



@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (25, 2, 10),
        (36, 2, 12),
        (9, 6, 18)
    ]
)        
 
def test_raiz(a , b, resultado_esperado):
    assert Calculator.raiz(a, b) == resultado_esperado



@pytest.mark.parametrize(
    ["a","b", "resultado_esperado"],
    [
        (-25, 2, "No se puede calcular la raiz de numeros negativos"),
        (-36, 2, "No se puede calcular la raiz de numeros negativos"),
        (-9, 6, "No se puede calcular la raiz de numeros negativos")
    ]
)        
 
def test_raiz_negativa(a , b, resultado_esperado):
    assert Calculator.raiz(a, b) == resultado_esperado