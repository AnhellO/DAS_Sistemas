import unittest
from Practica4 import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make(kind = "student", name = "foo")
        self.assertEqual(str(student), "Soy el alumno foo!, tengo -1 años y mi ID = XXXXXX")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make(kind = "teacher", name = "bar")
        self.assertEqual(str(teacher), "Soy el ticher bar!, tengo -1 años y mi ID = XXXXXX")
    
    def test_visitor_creation(self):
        visitor = SchoolMemberFactory.make(kind = "visitor", name = "fer")
        self.assertEqual(str(visitor), "Soy el visitante fer!, tengo -1 años y mi ID = XXXXXX")    
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make(kind = "tEaCHer", name = "baz")
        self.assertEqual(str(teacher), "Soy el ticher baz!, tengo -1 años y mi ID = XXXXXX")
        
    def test_invalid_type(self):
        invalid = SchoolMemberFactory.make(kind = "invalid", name = "foo")
        self.assertEqual(str(invalid), "[Error]: 'invalid' invalid kind")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make(kind = "inVaLiD", name = "bar")
        self.assertEqual(str(invalid), "[Error]: 'inVaLiD' invalid kind")
    
    def test_student_with_attributes(self):
        student = SchoolMemberFactory.make(kind = "student", name = "fer", age = 23, id_num = '002547')
        self.assertEqual(str(student), "Soy el alumno fer!, tengo 23 años y mi ID = 002547")   
    
    def test_student_with_incorrect_lenght_id(self):
        student = SchoolMemberFactory.make(kind = "student", name = "fer", age = 23, id_num = '2547')
        self.assertEqual(str(student), "Error! El tamaño del ID debe ser de 6 caracteres")
        


if __name__ == "__main__":
    unittest.main()