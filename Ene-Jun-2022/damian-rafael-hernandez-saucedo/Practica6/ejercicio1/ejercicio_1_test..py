import pytest

from ejercicio_1 import *

def test_add():
    branch1 = Composite("picture/")
    leaf11 = Leaf("photo.png")
    b3 = branch1.add(leaf11)
    assert b3 == "added successfully"

def test_remove():
    branch1 = Composite("picture/")
    leaf11 = Leaf("photo.png")
    branch1.add(leaf11)
    b2 = branch1.remove(leaf11)
    assert b3 == "added successfully"
    