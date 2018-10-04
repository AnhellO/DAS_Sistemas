# Clase que define a un instrumento
class instrumentoMusical(object): #Para nuestro caso, un instrumento tendrá 3 atributos, tipo, color, marca, precio aproximado 
	def __init__(self): 
		self.tipo = none 
		self.color = none 
		self.marca = none 
		self.precioAproximado = none
		# Algunos getters ... 
	def get_tipo(self): 
		return self.tipo 
	def get_color(self): 
		return self.color 
	def get_marca(self): 
		return self.marca 
	def get_precioAproximado(self): 
		return self.precioAproximado 

	def set_tipo(self, tipo): 
		self.tipo = tipo
	def set_color(self, color): 
		self.color = color
	def set_marca(self, marca): 
		self.marca = marca 
	def set_precioAproximado(self, precioAproximado): 
		self.precioAproximado = precioAproximado

	