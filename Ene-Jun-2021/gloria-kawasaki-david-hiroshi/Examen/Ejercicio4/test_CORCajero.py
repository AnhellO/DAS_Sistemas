import pytest

from CORCajero import CajeroATMChain

@pytest.mark.parametrize("expected", [
    (
        "entregando 1 billetes de 50\nentregando 1 billetes de 20\nentregando 1 billetes de 10\n"
    )
])
def test_1_billete_de_cada_uno(capfd, expected):
    ATM = CajeroATMChain()
    cantidad = 80
    ATM.chain1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "entregando 1 billetes de 20\n"
    )
])
def test_1_billete_de_20(capfd, expected):
    ATM = CajeroATMChain()
    cantidad = 20
    ATM.chain1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "entregando 1 billetes de 50\n"
    )
])
def test_1_billete_de_50(capfd, expected):
    ATM = CajeroATMChain()
    cantidad = 50
    ATM.chain1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "entregando 1 billetes de 10\n"
    )
])
def test_1_Billete_de_10(capfd, expected):
    ATM = CajeroATMChain()
    cantidad = 10
    ATM.chain1.handle(cantidad)
    out, _ = capfd.readouterr()
    assert out == expected

'''
import unittest
from CORCajero import CajeroATMChain as cajero

class TestClases(unittest.TestCase):
    def test_Just_1_buck_of_10(self):
        ATM = CajeroATMChain()
        cantidad = int(input("Cuánto desea sacar?: "))
        if cantidad < 10 or cantidad % 10 != 0:
            print("nel krnal, ingresa números positivos y en múltiplos de 10")
            exit()
        ATM.chain1.handle(cantidad)
        print("Ya vete krnal, ya le llamé a la clica")
'''