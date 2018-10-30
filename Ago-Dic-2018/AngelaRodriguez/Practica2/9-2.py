class Restaurante:


	def __init__ (self, nombre, tipo):

		self.nombre = nombre
		self.tipo = tipo

	def describe_restaurant(self):

		print(self.nombre.title() + self.tipo.title())

	def open_restaurant(self):

		print("El Restaurante está abierto")



restaurant= Restaurante('Las Golondrinas',' Mexicano')
restaurant2= Restaurante('Fu King',' Chino')
restaurant3= Restaurante('Donatucci',' Italiano')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

