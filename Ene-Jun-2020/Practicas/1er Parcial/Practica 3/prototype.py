class Oveja(object):
	"""docstring for Oveja"""
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

	def set_nombre(self, nombre):
		self.nombre=nombre

	def get_nombre(self):
		return self.nombre

	def set_tipo(self, tipo):
		self.tipo=tipo

	def get_tipo(self):
		return self.tipo
	def clone(self):
		return Oveja(self.nombre,self.tipo)