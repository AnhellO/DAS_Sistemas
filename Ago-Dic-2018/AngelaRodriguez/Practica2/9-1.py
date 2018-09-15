class Restaurante:


	def __init__ (self, nombre, tipo):

		self.nombre = nombre
		self.tipo = tipo

	def describe_restaurant(self):

		print(self.nombre.title() + self.tipo.title())

	def open_restaurant(self):

		print("El Restaurante está abierto")



restaurant= Restaurante('Las Golondrinas','Mexicano')


print("Nombre: " + str(restaurant.nombre))
print("Restaurante tipo: " + restaurant.tipo.title())
print(open_restaurant())
