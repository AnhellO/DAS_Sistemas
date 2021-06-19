import pytest

from chain_of_responsibility import CajeroATMChain

@pytest.mark.parametrize("amount, expected", [
    (
        250,
        "Entregando 5 billete(s) de $50\n"
    )
])
def test_only_50(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        40,
        "Entregando 2 billete(s) de $20\n"
    )
])
def test_only_20(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        10,
        "Entregando 1 billete(s) de $10\n"
    )
])
def test_only_10(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        90,
        "Entregando 1 billete(s) de $50\nEntregando 2 billete(s) de $20\n"
    )
])
def test_only_50_and_20(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        60,
        "Entregando 1 billete(s) de $50\nEntregando 1 billete(s) de $10\n"
    )
])
def test_only_50_and_10(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        30,
        "Entregando 1 billete(s) de $20\nEntregando 1 billete(s) de $10\n"
    )
])
def test_only_20_and_10(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("amount, expected", [
    (
        80,
        "Entregando 1 billete(s) de $50\nEntregando 1 billete(s) de $20\nEntregando 1 billete(s) de $10\n"
    )
])
def test_all(capfd, amount, expected):
    CajeroATMChain().chain1.handle(amount)
    out, _ = capfd.readouterr()
    assert out == expected