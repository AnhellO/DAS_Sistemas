from Instrumento_Musical import instrumentoMusical


class Bateria(instrumentoMusical):
 		#Esta clase hereda de la super clase instrumento Musical, solo definiremos su constructor

	def __init__(self, tipo, color, marca, precioAproximado, tamañoBombo, numeroPlatillos): 				
			self.tipo = tipo 
			self.color = color 
			self.marca = marca 
			self.precioAproximado = precioAproximado
			self.tamañoBombo = tamañoBombo
			self.numeroPlatillos = numeroPlatillos
			print ("Esta Batería "+marca+"\n"+ "Tiene un precio aproximado de:  "+str(precioAproximado))

	def afinarB(self):
		print(" Afinando Bateria ")

	def tocarB(self):
		print(" Pegandole a la bateria ")

	def get_tamañoBombo(self):
		return self.tamañoBombo

	def set_tamañoBombo(self, tamañoBombo):
		self.tamañoBombo = tamañoBombo

	def get_numeroPlatillos(self):
		return self.numeroPlatillos

	def set_numeroPlatillos(self, numeroPlatillos):
		self.numeroPlatillos = numeroPlatillos

	def __str__(self): 
		return "Informacion de un instrumento:\n1. Tipo: {}\n2. Color: {}\n3. Marca: {}\n4. Precio Aproximado: {}\n5. Tamaño Bombo: {}\n6. Número Platillos: {}\n".format(self.get_tipo(), self.get_color(), self.get_marca(), self.get_precioAproximado(), self.get_tamañoBombo(), self.get_numeroPlatillos())

