import unittest
from Practica4 import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make(kind = "student", name = "foo")
        self.assertEqual(str(student), "Soy el alumno foo!")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make(kind = "teacher", name = "bar")
        self.assertEqual(str(teacher), "Soy el maestro bar!")
    
    def test_visitor_creation(self):
        visitor = SchoolMemberFactory.make(kind = "visitor", name = "fer")
        self.assertEqual(str(visitor), "Soy el visitante fer!")    
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make(kind = "tEaCHer", name = "baz")
        self.assertEqual(str(teacher), "Soy el maestro baz!")
        
    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make(kind = "invalid", name = "foo")
        self.assertEqual(str(invalid), "Error! tipo 'invalid' invalido!")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make(kind = "inVaLiD", name = "bar")
        self.assertEqual(str(invalid), "Error! tipo 'inVaLiD' invalido!")
    
    def test_student_with_attributes(self):
        student = SchoolMemberFactory.make(kind = "student", name = "fer", age = 23, id_num = '02547')
        self.assertEqual(str(student), "Soy el alumno fer!, tengo 23 años y mi ID = 02547")    
        


if __name__ == "__main__":
    unittest.main()