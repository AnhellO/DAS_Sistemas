import abc

#Component
class ArchivoBase(metaclass=abc.ABCMeta):

	def __init__(self,nombre,tipo):
		self.nombre=nombre
		self,tipo=tipo

	@abc.abstractmethod
	def imprimeEstructura(self):
	    pass

	def getNombre(self):
		return self.nombre

	def getTipo(self):
		return self.tipo

#composit
class Dorectorio(ArchivoBase):
	def __init__(self,nombre,tipo):
						


