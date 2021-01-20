import unittest

from simple_factory import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", name="foo", age=24, id_num='ASD293R')
        self.assertEqual(str(student), "Soy el alumno foo!, tengo 24 años y mi ID = ASD293R")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", name="bar")
        self.assertEqual(str(teacher), "Soy el maestro bar!, tengo -1 años y mi ID = XXXXXX")
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", name="baz")
        self.assertEqual(str(teacher), "Soy el maestro baz!, tengo -1 años y mi ID = XXXXXX")
        
    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make("invalid", name="foo")
        self.assertEqual(str(invalid), "Error! tipo 'invalid' invalido!")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make("inVaLiD", name="bar")
        self.assertEqual(str(invalid), "Error! tipo 'inVaLiD' invalido!")
        


if __name__ == "__main__":
    unittest.main()
