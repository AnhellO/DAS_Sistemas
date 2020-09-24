import unittest
from School_Member import SchoolMemberFactory
# obj = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        kind = "Student"
        _name = "Jorge"
        edad = 13
        idd = "JAP001"
        student = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertEqual(str(student.MemberInfo()), "Soy el alumno {name}!, tengo {edad} años y mi ID = {idd}")
        
    def test_teacher_creation(self):
        kind = "Teacher"
        _name = "Laura"
        edad = 55
        idd = "LOP523"
        teacher = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertEqual(str(teacher.MemberInfo()), "Soy el profesor {name}!, tengo {edad} años y mi ID = {idd}")
        
    def test_creation_with_multiple_case(self):
        kind ="TeAcHER"
        _name ="Juan"
        edad =28
        idd = "JCA153"
        teacher = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertEqual(str(teacher), "Soy el maestro "+ name +" !")
        
    def test_invalid_type(self):
        kind = "student"
        _name = "Pepe"
        edad = 12
        idd = "JLO123"
        invalid = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertRaises(ValueError, invalid)
        
    def test_invalid_age(self):
        kind = "Student"
        _name = "Jorge"
        edad = -15
        idd = "123456"
        invalid = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertRaises(ValueError, invalid)

    def test_invalid_id(self):
        kind = "Student"
        _name = "Jorge"
        edad = 15
        idd = "12345678"
        invalid = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
        self.assertRaises(ValueError, invalid)
        
   

