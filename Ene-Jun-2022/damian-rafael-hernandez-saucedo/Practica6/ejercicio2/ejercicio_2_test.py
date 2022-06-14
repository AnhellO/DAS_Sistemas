import pytest

from ejercicio_2 import *

def test_get_nombre():
    oveja1 = Oveja1("Damian","3")
    assert oveja1.get_nombre() == "Damian"

def test_set_nombre():
    oveja1 = Oveja1("Damian","3")
    oveja1.set_nombre("Milton")
    assert oveja1.get_nombre() == "Milton"
    
def test_get_tipo():
    oveja1 = Oveja1("Damian","3")
    assert oveja1.get_tipo() == "3"

def test_set_tipo():
    oveja1 = Oveja1("Damian","3")
    oveja1.set_tipo("99")
    assert oveja1.get_tipo() == "99"

def test_clone():
    oveja1 = Oveja1("Damian","3")
    oveja2 = oveja1.clone()
    
    assert oveja2.get_nombre() == "Damian"
    assert oveja2.get_tipo() == "3"