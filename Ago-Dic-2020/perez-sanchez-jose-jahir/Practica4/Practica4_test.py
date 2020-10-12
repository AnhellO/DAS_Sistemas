import unittest
from Practica4 import SchoolMemberFactory, Teacher

class SchoolMemberFactoryTest(unittest.TestCase):
    def test_student_creation(self):
        student = SchoolMemberFactory.make("student", name = "foo")
        self.assertEqual(str(student), "Soy el alumno foo!, tengo -1 años y mi ID = XXXXXX")
        
    def test_teacher_creation(self):
        teacher = SchoolMemberFactory.make("teacher", name = "bar")
        self.assertEqual(str(teacher), "Soy el ticher bar!, tengo -1 años y mi ID = XXXXXX")
        
    def test_creation_with_multiple_case(self):
        teacher = SchoolMemberFactory.make("tEaCHer", name = "baz")
        self.assertEqual(str(teacher), "Soy el ticher baz!, tengo -1 años y mi ID = XXXXXX")
        
    def test_invalid_type(self): 
        invalid = SchoolMemberFactory.make("invalid", name = "foo")
        self.assertEqual(str(invalid), "Error! tipo 'invalid' invalido!")
        
    def test_invalid_with_multiple_case(self):
        invalid = SchoolMemberFactory.make("inVaLiD", name = "bar")
        self.assertEqual(str(invalid), "Error! tipo 'inVaLiD' invalido!")
    #T.D.D
    #Primero cree este test, pero me devolvia "Error! tipo 'director' invalido!", despues cree la class Director, ahora me devolvia "Soy Simon!, tengo -1 años y mi ID = XXXXXX"
    #Por culpa de la clases SchoolMember, entonces modifique la class Director para que sea un mensaje como director, al final cambie el mensaje final del test para que cuadrara como mi salida esperada
    def test_director_creation(self):
        director = SchoolMemberFactory.make("director", name = "Simon")
        self.assertEqual(str(director), "Soy el director Simon!, tengo -1 años y mi ID = XXXXXX")
    
    def test_student_attributes(self):
        student = SchoolMemberFactory.make("student", name = "Simona", age =17, id_num = "18316")
        self.assertEqual(str(student), "Soy el alumno Simona!, tengo 17 años y mi ID = 18316")


if __name__ == "__main__":
    unittest.main()