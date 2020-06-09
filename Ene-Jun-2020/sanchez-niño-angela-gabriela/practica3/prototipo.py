import copy
import abc
class prototipo(object):
	@abc.abstractmethod
	def clone(self):
		pass
	
class Oveja(prototipo):
	"""docstring for Oveja"""
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

	def set_nombre(self, nombre):
		self.nombre = nombre

	def get_nombre(self):
		return self.nombre

	def set_tipo(self, tipo):
		self.tipo = tipo

	def get_tipo(self):

		return self.tipo
	
	def clone(self):
		return self

	def __str__(self):
		return f'Nombre: {self.nombre}\nTipo: {self.tipo}'




if __name__ == "__main__":
	oveja1 = Oveja("dolly","1")
	print(oveja1)
	oveja2=copy.deepcopy(oveja1)
	oveja2.set_nombre ("dolly2")
	oveja2.set_tipo("2")
	print(oveja2)

	