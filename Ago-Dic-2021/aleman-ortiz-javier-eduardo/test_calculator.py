import pytest
from Calculator import *

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5,10,15),
        (-19,8,-11),
        (-19,-8,-27)
    ]

)
def test_suma(input_a, input_b, expected):
    calc=Calculator(input_a,input_b)
    assert calc.suma()==expected
    
@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5,10,-5),
        (-29,8,-37),
        (-29,-8,-21)
    ]

)

def test_resta(input_a, input_b, expected):
    calc=Calculator(input_a,input_b)
    assert calc.resta()==expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5,10,50),
        (-5,8,-40),
        (-7,-8,56)
    ]

)
def test_multiplicacion(input_a, input_b, expected):
    calc=Calculator(input_a,input_b)
    assert calc.Multiplicacion()==expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (10,5,2),
        (1/2,5,0.1),
        (-7,0,"Error")
    ]

)
def test_division(input_a, input_b, expected):
    calc=Calculator(input_a,input_b)
    assert calc.Division()==expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (10,5,100000),
        (1/2,5,1/32),
        (-7,5,-16807),
        (-5,-2,0.04)
    ]

)
def test_potencia(input_a, input_b, expected):
    calc=Calculator(input_a,input_b)
    assert calc.Potencia()==expected

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5,10,15.8113883),
        (-5,6,-12.24744871),
        (2,-5,"Error")
    ]

)
def test_raiz(input_a, input_b, expected):
    calc=Calculator(input_b,input_a)
    assert calc.Raiz()==expected