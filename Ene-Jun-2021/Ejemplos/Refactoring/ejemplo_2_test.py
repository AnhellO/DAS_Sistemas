import pytest

from ejemplo_2 import *

def test_suma():
    assert 4 == suma(2, 2)

def test_suma_extendida():
    assert 8 == suma(2, 2, 2, 2)

def test_factorial():
    assert 120 == factorial(5)