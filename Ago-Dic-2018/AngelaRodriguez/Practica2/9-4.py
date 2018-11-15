class Restaurante:


	def __init__ (self, nombre, tipo, number_served):

		self.nombre = nombre
		self.tipo = tipo
		self.number_served = 0

	def describe_restaurant(self):

		print(self.nombre.title() + self.tipo.title())


	def set_number_served(self):
		print(self.number_served.title())

	def increment_number_served(self):

		print(self.number_served.title)


restaurant= Restaurante('Las Golondrinas','Mexicano', '5')


print("Nombre: " + str(restaurant.nombre))
print("Restaurante tipo: " + restaurant.tipo.title())

print(number_served.title())
