import abc
class oveja():
	@abc.abstractmethod
	def clone(self):
		pass

class dolly(oveja):
	def __init__(self,nombre,tipo):
		self.nombre=nombre
		self.tipo=tipo
	def set_nombre(self,nombre):
		self.nombre=nombre
	def set_tipo(self,tipo):
		self.tipo=tipo
	def get_tipo(self):
		return self.tipo
	def get_nombre(self):
		return self.nombre
	def __str__(self):
		return f"Nombre: {self.nombre} \nTipo:{self.tipo}"
	def clone(self):
		return self

if __name__=="__main__":
	Oveja1=dolly("dolly", "domestica")
	Oveja2=Oveja1.clone()
	print(Oveja1)
	print("\n###############\n")
	print(Oveja2)
	Oveja2.set_nombre("Dude me llamo lupe")
	Oveja2.set_tipo("Dude soy salvaje")
	print(Oveja2)