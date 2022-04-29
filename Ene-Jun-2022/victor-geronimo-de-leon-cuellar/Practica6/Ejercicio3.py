class Persona(object):
	def __init__(self):
		self.nombre = None
		self.edad = None
		self.genero = None

	# Algunos getters ...
	def get_nombre(self):
		return self.nombre

	def get_edad(self):
		return self.edad

	def get_genero(self):
		return self.genero

	def __str__(self):
		return "Informacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}".format(
			n=self.get_nombre(), e=self.get_edad(), g=self.get_genero())

class Femenino(Persona): 
	
	def __init__(self, nombre, edad, genero):
		self.nombre  = nombre
		self.edad = edad
		self.genero = genero
		print ("Mujer "+nombre+" su edad: "+str(edad))


class Masculino(Persona): 

	def __init__(self, nombre, edad, genero):
		self.nombre = nombre
		self.edad = edad
		self.genero = genero
		print ("Hombre "+nombre+" su edad: "+str(edad))

class Factoria(object):

	def get_persona(self, nombre, genero, edad):
		
		if (genero is 'F'): 
			return Femenino(nombre, edad, genero)
		elif (genero is 'M'):
			return Masculino(nombre, edad, genero)