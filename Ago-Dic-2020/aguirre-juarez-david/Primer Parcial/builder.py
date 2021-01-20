
class Pizza:
	def __init__(self, length):
		self.ingredients = []
		self.__length = length

	def __str__(self):
		ingredients = ""
		for m in self.ingredients:
			ingredients += f"{m} y "

		return f'Mi pizza es de {self.__length}" con los siguientes ingredientes: {ingredients[:-3].replace(" y", ",", len(self.ingredients) - 2)}'

class PizzaBuilder:
	def __init__(self, length):
		self.__pizza = Pizza(length)
		self.__pizza.ingredients = ["salsa de tomate", "queso"]

	def build(self):
		return self.__pizza

	def addCheese(self):
		self.__pizza.ingredients.append("doble queso")

	def addPepperoni(self):
		self.__pizza.ingredients.append("pepperoni")

	def addSalami(self):
		self.__pizza.ingredients.append("salami")

	def addPimientos(self):
		self.__pizza.ingredients.append("pimientos")

	def addCheese(self):
		self.__pizza.ingredients.append("doble queso")

	def addCebolla(self):
		self.__pizza.ingredients.append("cebolla")		
	
	def addChampiñones(self):
		self.__pizza.ingredients.append("champiñones")