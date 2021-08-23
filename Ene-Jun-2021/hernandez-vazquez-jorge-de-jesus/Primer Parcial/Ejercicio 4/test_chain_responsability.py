import pytest
#import unittest
from unittest import mock 
from chain_responsability import Cajero50ConcreteHandler, Cajero20ConcreteHandler, Cajero10ConcreteHandler


    # Parametrizamos la prueba de los billetes de 50
    # Capturamos la salida del "Cajero50ConcreteHandler().handle(150)"
    # Y la comparamos con nuestro valor esperado "expected"
@pytest.mark.parametrize("expected", ["Cambio: 3 billetes de $50\n"])
def test_cajero_50(capfd, expected):
    Cajero50ConcreteHandler().handle(150)
    out, _ = capfd.readouterr()
    assert out == expected


    # Parametrizamos la prueba de los billetes de $20    
    # Capturamos la salida del "Cajero20ConcreteHandler().handle(120)"
    # Y la comparamos con nuestro valor esperado "expected"
@pytest.mark.parametrize("expected", ["Cambio: 6 billetes de $20\n"])
def test_cajero_20(capfd, expected):
    Cajero20ConcreteHandler().handle(120)
    out, _ = capfd.readouterr( )
    assert out == expected


    # Parametrizamos la prueba de los billetes de $10
    # Capturamos la salida del "Cajero50ConcreteHandler().handle(130)"
    # Y la comparamos con nuestro valor esperado "expected"
@pytest.mark.parametrize("expected", ["Cambio: 13 billetes de $10\n"])
def test_cajero_10(capfd, expected):
    Cajero10ConcreteHandler().handle(130)
    out, _ = capfd.readouterr()
    assert out == expected

#pytest -q test_chain_responsability.py 