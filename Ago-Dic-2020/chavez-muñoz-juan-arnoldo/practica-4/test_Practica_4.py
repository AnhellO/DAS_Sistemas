from Practica_4 import Secretary, Student, Teacher, SchoolMemberFactory
import pytest

def test_secretary():
    secretary = Secretary()
    expected = "Secretari@"
    real = secretary.identity()
    assert expected == real

def test_teacher():
    t = Teacher()
    expected = "Maestr@"
    real = t.identity()
    assert expected == real
    
def test_student():
    stu = Student()
    expected = "Estudiante"
    real = stu.identity()
    assert expected == real

def test_school_member_factory():
    obj = SchoolMemberFactory.make(kind='Teacher', name='jacky', age=22 , id_num='070KGP')
    esperada = "Soy el/la Maestr@ jacky!, tengo 22 años y mi ID = 070KGP"
    real = str(obj)
    assert real == esperada
    
def test_school_member_factory2():
    obj = SchoolMemberFactory.make(kind='Student', name='Leo', age=24 , id_num='070KGP')
    esperada = "Soy el/la Estudiante Leo!, tengo 24 años y mi ID = 070KGP"
    real = str(obj)
    assert real == esperada

def test_school_member_factory3():
    obj = SchoolMemberFactory.make(kind='Secretary', name='Israel', age=25 , id_num='070KGP')
    esperada = "Soy el/la Secretari@ Israel!, tengo 25 años y mi ID = 070KGP"
    real = str(obj)
    assert real == esperada
