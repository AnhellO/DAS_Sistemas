import pytest
from abc import ABCMeta, abstractclassmethod

from chain_of_responsability import CajeroATMChain

@pytest.mark.parametrize("expected", [
    (
       "Tendras: 5 billetes de 20\n"
    )
])
def test_cambio_1(capfd, expected):
    x = CajeroATMChain()
    billete_a_cambiar = int(100)
    x.chain2.handle(billete_a_cambiar)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
       "Tendras: 315 billetes de 50\nTendras: 1 billetes de 20\n"
    )
])
def test_cambio_2(capfd, expected):
    x = CajeroATMChain()
    billete_a_cambiar = int(15770)
    x.chain1.handle(billete_a_cambiar)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
       "Tendras: 1 billetes de 50\nTendras: 1 billetes de 10\n"
    )
])
def test_cambio_3(capfd, expected):
    x = CajeroATMChain()
    billete_a_cambiar = int(60)
    x.chain1.handle(billete_a_cambiar)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
       "Tendras: 2 billetes de 50\nTendras: 1 billetes de 20\nTendras: 1 billetes de 10\n"
    )
])
def test_cambio_4(capfd, expected):
    x = CajeroATMChain()
    billete_a_cambiar = int(130)
    x.chain1.handle(billete_a_cambiar)
    out, _ = capfd.readouterr()
    assert out == expected
    
@pytest.mark.parametrize("expected", [
    (
       "No es posible hacer el cambio de billetes\n"
    )
])
def test_cambio_5(capfd, expected):
    x = CajeroATMChain()
    billete_a_cambiar = int(5)
    x.chain1.handle(billete_a_cambiar)
    out, _ = capfd.readouterr()
    assert out == expected
    