import pytest

from ejercicio_3 import *

def test_FireFighter():
    worker = FireFighter()
    assert worker.work() == "FireFighter is working"

def test_Lumberjack():
    worker = Lumberjack()
    assert worker.work() == "Lumberjack is working"
    
def test_Postman():
    worker = Postman()
    assert worker.work() == "Postman is working"
    
def test_Manager_work():
    worker = Manager()
    assert worker.work() == "Manager is working"
    
def test_Manager_relax():
    worker = Manager()
    assert worker.relax() == "Manager is relaxing"