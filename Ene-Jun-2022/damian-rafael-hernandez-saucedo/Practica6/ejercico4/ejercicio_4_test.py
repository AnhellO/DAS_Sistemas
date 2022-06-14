import pytest
from ejercicio_4 import *


def test_Client():
    items = [
        Element_A("Student"),
        Element_A("Teacher"),
        Element_B("Student"),
        Element_B("Teacher"),        
    ]
    expected = ["He's a Student Element A", "He's a Teacher Element A", "He's a Student Element B", "He's a Teacher Element B"]
    assert Client(items) == expected
    

def test_ConcreteVisitor():
    items = [
        Element_A("Student")
    ]
    Client(items)
    visitor1 = ConcretVisitor()
    visitor2 = visitor1.visit(items[0])
    assert visitor2 == "He's a Student Element A"


def test_Element_A():
    elementA = Element_A("Student")
    assert elementA.get_name() == "Student Element A"
    

def test_Element_B():
    elementA = Element_A("Teacher")
    assert elementA.get_name() == "Teacher Element A"