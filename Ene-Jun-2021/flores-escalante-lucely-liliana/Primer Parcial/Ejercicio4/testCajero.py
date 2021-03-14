import pytest
from Cajero import CajeroATMChain


@pytest.mark.parametrize("expected", [
    (
        "1 billete(s) de 50\n1 billete(s) de 20\n1 billete(s) de 10\n"
    )
])
def test_uno_de_cada_uno(capfd, expected):
    cajero = CajeroATMChain()
    monto = 80
    cajero.chain1.handle(monto)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "1 billete(s) de 20\n"
    )
])
def test_1_billete_de_50(capfd, expected):
    ATM = CajeroATMChain()
    monto = 50
    ATM.chain1.handle(monto)
    out, _ = capfd.readouterr()
    assert out == expected