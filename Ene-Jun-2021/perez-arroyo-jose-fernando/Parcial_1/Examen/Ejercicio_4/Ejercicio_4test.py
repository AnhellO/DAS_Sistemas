import pytest

from Ejercicio_4 import ATMChain

@pytest.mark.parametrize("expected", [
    (
        "Compensacion 1 $50\nCompensacion 1 $20\nCompensacion 1 $10\n"
    )
])
def test_X1(capfd, expected):
    ATM = ATMChain()
    cantidad = 80
    ATM.chainof1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "Compensacion 6 $50"
    )
])
def test_X1(capfd, expected):
    ATM = ATMChain()
    cantidad = 300
    ATM.chainof1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected