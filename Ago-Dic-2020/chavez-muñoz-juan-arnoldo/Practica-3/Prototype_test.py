from Prototype import DSA, Courses_At_GFG_Cache, SDE, DYAS
import pytest

def test_Courses_At_GFG_Cache():
    Courses_At_GFG_Cache.load() 
    sde = Courses_At_GFG_Cache.get_course("1") 
    assert sde.get_id()

def test_load():
    sde = SDE() 
    sde.set_id("1") 
    Courses_At_GFG_Cache.cache[sde.get_id()] = sde 
    assert SDE.get_id(sde)

def test_get_course():
    dyas = DYAS()
    dyas = Courses_At_GFG_Cache.get_course("4")
    assert dyas

def test_get_course2():
    dyas = DYAS()
    dyas = Courses_At_GFG_Cache.get_course("8")
    assert dyas 

def test_course_nsdeDYAS():
    dyas = DYAS()
    assert DYAS.course(dyas)

def test_course_nsdeDSA():
    dsa = DSA()
    assert DSA.course(dsa)
