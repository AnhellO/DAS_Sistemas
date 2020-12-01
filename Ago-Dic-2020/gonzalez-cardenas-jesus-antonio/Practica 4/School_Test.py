import unittest
from School_Member import school_member_factory

class school_member_factoryTest(unittest.TestCase):
    def test_student_creation(self):
        kind = "Student"
        _name = "Jorge"
        edad = 13
        idd = "JAP001"
        student = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertEqual(str(student), f"Soy el alumno {_name}!, tengo {edad} años y mi ID = {idd}")
        
    def test_teacher_creation(self):
        kind = "Teacher"
        _name = "Laura"
        edad = 55
        idd = "LOP523"
        teacher = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertEqual(str(teacher), f"Soy el profesor {_name}!, tengo {edad} años y mi ID = {idd}")
        
    def test_creation_with_multiple_case(self):
        kind ="TeAcHER"
        _name ="Juan"
        edad =28
        idd = "JCA153"
        with self.assertRaises(ValueError):
            teacher = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
        
    def test_invalid_type(self):
        kind = "student"
        _name = "Pepe"
        edad = 12
        idd = "JLO123"
        with self.assertRaises(ValueError):
            invalid = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
        
    def test_invalid_age(self):
        kind = "Student"
        _name = "Jorge"
        edad = -15
        idd = "123456"
        with self.assertRaises(ValueError):
            invalid = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)

    def test_invalid_id(self):
        kind = "Student"
        _name = "Jorge"
        edad = 15
        idd = "12345678"
        with self.assertRaises(ValueError):
            invalid = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
   

if __name__ == '__main__':
    unittest.main()