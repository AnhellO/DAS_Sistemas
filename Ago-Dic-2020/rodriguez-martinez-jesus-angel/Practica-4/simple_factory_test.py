import unittest
from simple_factory import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):

    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", name="profe")
        self.assertEqual(str(teacher), "¡Mi nombre es profe!, soy Maestro, tengo -1 años y mi ID es XXXXXX")

    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", name="estudi", age=22, id_num='070KGP')
        self.assertEqual(str(student), "¡Mi nombre es estudi!, soy Estudiante, tengo 22 años y mi ID es 070KGP")

    def test_director_creation(self):
        student = SchoolMemberFactory.make("student", name="dire")
        self.assertEqual(str(student), "¡Mi nombre es dire!, soy Estudiante, tengo -1 años y mi ID es XXXXXX")
               
    def test_creation_with_no_name(self):
        teacher = SchoolMemberFactory.make("tEaCHer")
        self.assertEqual(str(teacher), "¡Mi nombre es !, soy Maestro, tengo -1 años y mi ID es XXXXXX")

    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", name="bar")
        self.assertEqual(str(teacher), "¡Mi nombre es bar!, soy Maestro, tengo -1 años y mi ID es XXXXXX")

    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make("invalid", name="bar")
        self.assertEqual(str(invalid), "[Error]: 'invalid' invalid role")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make("inVaLiD", name="bar")
        self.assertEqual(str(invalid), "[Error]: 'inVaLiD' invalid role")

if __name__ == "__main__":
    unittest.main()