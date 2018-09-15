class Restaurant:
	def __init__(self, nombre='Felipe', cuisine_type='no se', estado=''):
		self.nombre=nombre
		self.cuisine_type=cuisine_type
		self.estado=estado

	def __str__(self):
		return('Nombre:{} \nType: {}  \nestado: {}'.format(self.nombre, self.cuisine_type, self.estado))

	def open_restaurant(self):
		estado=(sel.estado)
		print(estado)

describe_restaurant=Restaurant()
print(describe_restaurant)

open_restaurant=Restaurant('Doña','Gorditas','Abierto')
print(open_restaurant)
