import pytest

from ejercicio_2 import *

def test_get_nombre():
    oveja1 = Oveja1("juan","3")
    assert oveja1.get_nombre() == "juan"

def test_set_nombre():
    oveja1 = Oveja1("juan","3")
    oveja1.set_nombre("pepe")
    assert oveja1.get_nombre() == "pepe"
    
def test_get_tipo():
    oveja1 = Oveja1("juan","3")
    assert oveja1.get_tipo() == "3"

def test_set_tipo():
    oveja1 = Oveja1("juan","3")
    oveja1.set_tipo("99")
    assert oveja1.get_tipo() == "99"

def test_clone():
    oveja1 = Oveja1("juan","3")
    oveja2 = oveja1.clone()
    
    assert oveja2.get_nombre() == "juan"
    assert oveja2.get_tipo() == "3"