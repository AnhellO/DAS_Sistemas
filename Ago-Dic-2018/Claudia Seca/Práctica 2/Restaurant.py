class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	#Imprime atributos
	def describe_restaurant(self):
		print("The Restaurant name is: {}".format(self.restaurant_name))
		print("The Cuisine Type is: {}".format(self.cuisine_type))

	def open_restaurant(self):
		print("The Restaurant {} is Open".format(self.restaurant_name))

restaurant = Restaurant("Honey Moon", "Mediterranea")
print(restaurant.restaurant_name,",", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


