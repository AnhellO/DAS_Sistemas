import unittest

from Practica4 import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", name="Panther")
        self.assertEqual(str(student), "Soy el estudiante Panther!, tengo 22 años y mi ID = 070KGP")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", name="Crow")
        self.assertEqual(str(teacher), "Soy el profesor Crow!, tengo 22 años y mi ID = 070KGP")

    def test_coach_creation(self):
        coach = SchoolMemberFactory.make("coach", name="Noir")
        self.assertEqual(str(coach), "Soy el Coach Noir!, tengo 22 años y mi ID = 070KGP")
               
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", name="Skull")
        self.assertEqual(str(teacher), "Soy el profesor Skull!, tengo 22 años y mi ID = 070KGP")
        
    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make("invalid", name="Joker")
        self.assertEqual(str(invalid), "# ERROR # Esa fucion no es valida. intente: Student, Teacher, Coach.")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make("inVaLiD", name="Oracle")
        self.assertEqual(str(invalid), "# ERROR # Esa fucion no es valida. intente: Student, Teacher, Coach.")

if __name__ == "__main__":
    unittest.main()