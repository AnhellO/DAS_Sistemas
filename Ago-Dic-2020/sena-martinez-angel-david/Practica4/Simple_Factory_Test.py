import unittest
from Simple_Factory import SchoolMemberFactory

class SchoolMemberFactoryTest(unittest.TestCase):
	def test_creacion_estudiante(self):
		student = SchoolMemberFactory.make("student", name="Juan")
		self.assertEqual(str(student), "Me llamo Juan!, soy Estudiante, tengo -1 años y mi ID = XXXXXX")

	def test_creacion_maestro(self):
		teacher = SchoolMemberFactory.make("teacher", name="Pedro")
		self.assertEqual(str(teacher), "Me llamo Pedro!, Soy el Maestro, tengo -1 años y mi ID = XXXXXX")

	def test_creacion_varios_casos(self):
		teacher = SchoolMemberFactory.make("tEaCHer", name="David")
		self.assertEqual(str(teacher), "Me llamo David!, Soy el Maestro, tengo -1 años y mi ID = XXXXXX")

	def test_estudiante_con_atributos(self):
		teacher = SchoolMemberFactory.make("teacher", name="Angel", age=25, id_num='ABCDEF')
		self.assertEqual(str(teacher), "Me llamo Angel!, Soy el Maestro, tengo 25 años y mi ID = ABCDEF")

	def test_creacion_trabajador(self):
		secretary = SchoolMemberFactory.make("worker", name="Julio", age=23)
		self.assertEqual(str(secretary), "Me llamo Julio!, Soy el trabajador, tengo 23 años y mi ID = XXXXXX")

	def test_tipo_invalido(self):
		invalid = SchoolMemberFactory.make("invalid", name="Juam")
		self.assertEqual(str(invalid), "Error! tipo 'Invalid' invalido!")

	def test_invalido_con_multipes_casos(self):
		invalid = SchoolMemberFactory.make("inVaLiD", name="Hugp")
		self.assertEqual(str(invalid), "Error! tipo 'Invalid' invalido!")

	def test_invalido_id(self):
		invalid = SchoolMemberFactory.make("student", name="Juan", age=25, id_num='ABCF')
		self.assertEqual(str(invalid), "Error! formato de ID invalido!")

	def test_invalido_nombre_de_clase(self):
		invalid = SchoolMemberFactory.make("SchoolStudent", name="Juan")
		self.assertEqual(str(invalid), "Error! tipo 'SchoolStudent' invalido!")

	def test_invalido_con_tipo_vacio(self):
		invalid = SchoolMemberFactory.make("", name="Juan")
		self.assertEqual(str(invalid), "Error! tipo '' invalido!")

if __name__ == "__main__":
	unittest.main() 