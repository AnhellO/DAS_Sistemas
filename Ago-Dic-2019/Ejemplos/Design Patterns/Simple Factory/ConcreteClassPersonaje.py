class ConcreteClassPersonaje(object):
	"""docstring for Personaje"""
	def __init__(self, tipo, nombre, hab_especial):
		self._tipo = tipo
		self._nombre = nombre
		self._hab_especial = hab_especial

	def set_tipo(self, tipo):
		self._tipo = tipo

	def get_tipo(self):
		return self._tipo

	def set_nombre(self, nombre):
		self._nombre = nombre

	def get_nombre(self):
		return self._nombre

	def set_hab_especial(self, hab_especial):
		self._hab_especial = hab_especial

	def get_hab_especial(self):
		return self._hab_especial

	def __str__(self):
		return '''
			Tipo: {}\nNombre: {}\nHabilidad Especial: {}
		'''.format(self._tipo, self._nombre, self._hab_especial).strip()
