import unittest
from School_Member import SchoolMemberFactory
# obj = SchoolMemberFactory.make(kind, name=_name, age=int(edad), id=idd)
class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        kind = "Student"
        name = "Jorge"
        edad = 13
        idd = "JAP001"
        student = SchoolMemberFactory.make("student")
        self.assertEqual(str(student), "Soy el alumno "+ name +" !")
        
    def test_teacher_creation(self):
        kind = "Teacher"
        name = "Laura"
        edad = 55
        idd = "LOP523"
        teacher = SchoolMemberFactory.make("teacher", "bar")
        self.assertEqual(str(teacher), "Soy el maestro "+ name +" !")
        
    def test_creation_with_multiple_case(self):
        kind =
        name =
        edad =
        idd =
        teacher = SchoolMemberFactory.make("tEaCHer", "baz")
        self.assertEqual(str(teacher), "Soy el maestro baz!")
        
    def test_invalid_type(self):
        kind =
        name =
        edad =
        idd =
        invalid = SchoolMemberFactory.make("invalid", "foo")
        self.assertEqual(str(invalid), "Error! tipo 'invalid' invalido!")
        
    def test_invalid_with_multiple_case(self):
        kind =
        name =
        edad =
        idd =
        invalid = SchoolMemberFactory.make("inVaLiD", "bar")
        self.assertEqual(str(invalid), "Error! tipo 'inVaLiD' invalido!")
        

