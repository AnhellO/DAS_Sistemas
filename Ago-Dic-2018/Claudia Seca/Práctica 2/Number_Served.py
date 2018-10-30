class Restaurant():

	def __init__(self, restaurant_name, cuisine_type, number_served = 0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served


	#Imprime atributos
	def describe_restaurant(self):
		print("The Restaurant name is: {}".format(self.restaurant_name))
		print("The Cuisine Type is: {}".format(self.cuisine_type))

	def open_restaurant(self):
		print("The Restaurant {} is Open".format(self.restaurant_name))

	def set_number_served(self,number):
		self.number_served = number

	def increment_number_served(self,otherNumber):
		self.number_served += otherNumber

restaurant = Restaurant("Honey Moon", "Mediterranea")
print("Los clientes despachados: {} ".format(restaurant.number_served))
restaurant.number_served = 13
print("Los clientes despachados: {} ".format(restaurant.number_served))
restaurant.set_number_served(42)
print("Los clientes despachados: {} ".format(restaurant.number_served))
restaurant.increment_number_served(8)
print("Los clientes despachados: {} ".format(restaurant.number_served))
