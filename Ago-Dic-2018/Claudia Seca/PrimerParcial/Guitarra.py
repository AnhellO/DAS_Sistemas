from Instrumento_Musical import instrumentoMusical


class Guitarra(instrumentoMusical):
 		#Esta clase hereda de la super clase Instrumento Musical, solo definiremos su constructor

	def __init__(self, tipo, color, marca, precioAproximado, tamañoDiapason, numeroCuerdas): 				
			self.tipo = tipo 
			self.color = color 
			self.marca = marca 
			self.precioAproximado = precioAproximado
			self.tamañoDiapason = tamañoDiapason
			self.numeroCuerdas = numeroCuerdas
			print ("Esta Guitarra "+marca+" Tiene un precio aproximado de:  "+str(precioAproximado))

	def afinarP(self):
		print(" Afinando Guitarra ")

	def tocarP(self):
		print(" Playing la guitar ")

	def get_tamañoDiapason(self):
		return self.tamañoDiapason

	def set_tamañoDiapason(self, tamañoDiapason):
		self.tamañoDiapason = tamañoDiapason

	def get_numeroCuerdas(self):
		return self.numeroCuerdas

	def set_numeroCuerdas(numeroCuerdas):
		self.numeroCuerdas = numeroCuerdas

	def __str__(self): 
		return "Informacion de un instrumento:\n1. Tipo: {}\n2. Color: {}\n3. Marca: {}\n4. Precio Aproximado:{}\n5. Tamaño Diapason:{}\n6. Número de Cuerdas".format(self.get_tipo(), self.get_color(), self.get_marca(), self.get_precioAproximado(), self.get_tamañoDiapason(), self.get_numeroCuerdas())

