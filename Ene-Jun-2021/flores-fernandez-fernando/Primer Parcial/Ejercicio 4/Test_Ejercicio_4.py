import pytest
from Ejercicio_4 import *
@pytest.mark.parametrize("expected", [
    (
        "Dispensando 2 billetes de $50\nDispensando 1 billetes de $20\nDispensando 1 billetes de $10\n"
    )
])

def test_chain_completo(capfd, expected):
    ATM = CajeroATMChain()
    ATM.chain1.handle(130)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "Dispensando 6 billetes de $20\nDispensando 1 billetes de $10\n"
    )
])

def test_chain_20_y_10(capfd, expected):
    ATM = CajeroATMChain()
    ATM.chain2.handle(130)
    out, _ = capfd.readouterr()
    assert out == expected
@pytest.mark.parametrize("expected", [
    (
        "Dispensando 13 billetes de $10\n"
    )
])

def test_chain_10(capfd, expected):
    ATM = CajeroATMChain()
    ATM.chain3.handle(130)
    out, _ = capfd.readouterr()
    assert out == expected
    