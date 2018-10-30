class Restaurant():
	def __init__(self, nombre, cuisine_type, number_server):
		self.nombre=nombre.title()
		self.cuisine_type=cuisine_type
		self.number_server=number_server
	def __str__(self):
		return('Name:{}, \nType:{}, \nServicio:{}'.format(self.nombre, self.cuisine_type, self.number_server))


	def number(self):
		servicios="Nombre:" + self.nombre + "\nTipo:" + self.cuisine_type + "\nServicios:" + str(self.number_server)
		print(servicios)

	def incremento(self):
		incre=int(input("Cuantos servicios incrementaron?"))
		aux=(self.number_server+ incre)
		servicios="Nombre:" + self.nombre + "\nTipo:" + self.cuisine_type + "\nServicios:" +  str(aux)
		print(servicios)
	
#restaurante=Restaurant('China','Food') comentariado para implementar los ejercicios
#print(restaurante)

serv1=Restaurant('Chinesse','Food', '4')
serv1.number()

print("\n")
serv2=Restaurant('Fonda', 'comidap/llevar', 15)
serv2.number()

print("\n")
serv2.incremento()  #El incremento lo hace tomando los paramentros de Serv2