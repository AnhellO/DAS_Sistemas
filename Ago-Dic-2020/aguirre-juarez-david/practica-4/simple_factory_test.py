import unittest
from simple_factory import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
	def test_student_creation(self):
		student = SchoolMemberFactory.make("student", name="foo")
		self.assertEqual(str(student), "Me llamo foo!, soy Estudiante, tengo -1 años y mi ID = XXXXXX")

	def test_teacher_creation(self):
		teacher = SchoolMemberFactory.make("teacher", name="bar")
		self.assertEqual(str(teacher), "Me llamo bar!, soy Maestro, tengo -1 años y mi ID = XXXXXX")

	def test_creation_with_multiple_case(self):
		teacher = SchoolMemberFactory.make("tEaCHer", name="baz")
		self.assertEqual(str(teacher), "Me llamo baz!, soy Maestro, tengo -1 años y mi ID = XXXXXX")

	def test_student_with_attributes(self):
		teacher = SchoolMemberFactory.make("teacher", name="baz", age=25, id_num='ABCDEF')
		self.assertEqual(str(teacher), "Me llamo baz!, soy Maestro, tengo 25 años y mi ID = ABCDEF")

	def test_secretary_creation(self):
		secretary = SchoolMemberFactory.make("secretary", name="bar", age=23)
		self.assertEqual(str(secretary), "Me llamo bar!, soy Secretario, tengo 23 años y mi ID = XXXXXX")

	def test_secretary_upper_creation(self):
		secretary = SchoolMemberFactory.make("SECRETARY", name="baz", age=23)
		self.assertEqual(str(secretary), "Me llamo baz!, soy Secretario, tengo 23 años y mi ID = XXXXXX")

	def test_invalid_type(self):
		invalid = SchoolMemberFactory.make("invalid", name="foo")
		self.assertEqual(str(invalid), "Error! tipo 'Invalid' invalido!")

	def test_invalid_with_multiple_case(self):
		invalid = SchoolMemberFactory.make("inVaLiD", name="bar")
		self.assertEqual(str(invalid), "Error! tipo 'Invalid' invalido!")

	def test_invalid_id(self):
		invalid = SchoolMemberFactory.make("student", name="baz", age=25, id_num='ABCF')
		self.assertEqual(str(invalid), "Error! formato de ID invalido!")

	def test_invalid_with_class_name(self):
		invalid = SchoolMemberFactory.make("SchoolStudent", name="foo")
		self.assertEqual(str(invalid), "Error! tipo 'SchoolStudent' invalido!")

	def test_invalid_with_empty_type(self):
		invalid = SchoolMemberFactory.make("", name="foo")
		self.assertEqual(str(invalid), "Error! tipo '' invalido!")

if __name__ == "__main__":
	unittest.main()