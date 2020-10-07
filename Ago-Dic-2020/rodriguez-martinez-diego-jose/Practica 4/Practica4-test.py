import unittest
from Practica4 import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", name = "foo")
        self.assertEqual(str(student), "Soy el Student foo!, tengo -1 años y mi ID = XXXXXX")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", name = "bar")
        self.assertEqual(str(teacher), "Soy el Teacher bar!, tengo -1 años y mi ID = XXXXXX" )

    def test_janitor_creation(self):
        janitor = SchoolMemberFactory.make("Janitor", name = "foo")
        self.assertEqual(str(janitor),"Soy el Janitor foo!, tengo -1 años y mi ID = XXXXXX")
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", name = "foo")
        self.assertEqual(str(teacher), "Soy el Teacher foo!, tengo -1 años y mi ID = XXXXXX")
        
    def test_creation_no_name(self):
        teacher = SchoolMemberFactory.make("tEaCHer", age = 22)
        self.assertEqual(str(teacher), "Soy el Teacher !, tengo 22 años y mi ID = XXXXXX")

    def test_invalid_type(self):
        with self.assertRaisesWithMessage(ValueError):
            SchoolMemberFactory.make("invalid", name = "foo")
        
    def test_invalid_with_multiple_case(self):
        with self.assertRaisesWithMessage(ValueError):
           SchoolMemberFactory.make("InVaLID", name = "foo")
        
        
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()