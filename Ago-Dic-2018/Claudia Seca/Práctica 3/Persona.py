# Clase que define a una persona 
class Persona(object): #Para nuestro caso, una persona tendrá un nombre, una edad y un genero, por lo general en Java esta clase sería una 'interfaz' """ 
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
		return "Informacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}".format(n=self.get_nombre(), e=self.get_edad(), g=self.get_genero())
