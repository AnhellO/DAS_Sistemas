from ConcreteClassPersonaje import ConcreteClassPersonaje

class SimpleFactory(object):
	"""docstring for SimpleFactory"""
	@staticmethod
	def makeConcreteClassPersonaje(**atributos):
		tipo = atributos.get('tipo')
		nombre = atributos.get('nombre')
		hab_especial = atributos.get('hab_especial')
		return ConcreteClassPersonaje(tipo, nombre, hab_especial)
		