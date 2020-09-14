import unittest

from simple_factory import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", "foo")
        self.assertEqual(str(student), "Soy el alumno foo!")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", "bar")
        self.assertEqual(str(teacher), "Soy el maestro bar!")
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", "baz")
        self.assertEqual(str(teacher), "Soy el maestro baz!")
        
    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make("invalid", "foo")
        self.assertEqual(str(invalid), "Error! tipo 'invalid' invalido!")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make("inVaLiD", "bar")
        self.assertEqual(str(invalid), "Error! tipo 'inVaLiD' invalido!")
        


if __name__ == "__main__":
    unittest.main()
