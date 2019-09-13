class Restaurant():
	def __init__(self, nombre, cuisine_type):
		self.nombre=nombre.title()
		self.cuisine_type=cuisine_type
		

	def describe_restaruant(self):
		aux="Nombre:"+ self.nombre + "\n"+"Tipo:"+ self.cuisine_type
		print("\n" + aux)

	def open_restaurant(self):
		aux="El" + self.nombre + "esta Abierto"
		print("\n"+ aux) 

rest=Restaurant('Servicio express', 'pizza')
rest.describe_restaruant()
rest.open_restaurant()

rest2=Restaurant("Felipe", " tortas")
rest2.describe_restaruant()

rest3=Restaurant("china","comida")
rest3.describe_restaruant()

rest4=Restaurant("el paseo", "comidaMexicana")
rest4.describe_restaruant()

 