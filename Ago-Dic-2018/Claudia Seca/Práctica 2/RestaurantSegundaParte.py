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

restaurant2 = Restaurant("Los Comales", "Mexicana")
print(restaurant2.restaurant_name,",", restaurant2.cuisine_type)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("Toscana", "Italiana")
print(restaurant3.restaurant_name,",", restaurant3.cuisine_type)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

