from abc import ABCMeta, abstractmethod


class Instrumento_musical:
	def __init__(self, clasificacion='', tamaño='', nombre=''):
		self.clasificacion=clasificacion
		self.tamaño=tamaño
		self.nombre=nombre
	def __str__(self):
		return ('Instrumento musical: \n de clasificacion: {} \n tamaño: {} \n nombre: {}'.format(self.clasificacion, self.tamaño, self.nombre))
	
	#@abstractmethod
	def TipoGuitarra(self):
		pass
	#@abstractmethod
	def Afinar(self):
		pass
	#@abstractmethod
	def TipoBaqueta(self):
		pass
	#@abstractmethod
	def PrecioBateria(self):
		pass

class Guitarra(Instrumento_musical):
	def __init__(self,clasificacion,tamaño,nombre,cuerdas='',tipo='',color=''):
		Instrumento_musical.__init__(self,clasificacion,tamaño,nombre)
		self.cuerdas=cuerdas
		self.tipo=tipo
		self.color=color

	def __str__(self):
		return('\n Guitarra:\n de clasificacion: {} \n tamaño: {} \n nombre: {} \n con cuerdas: {} \n tipo: {} \n de color: {}'.format(self.clasificacion, self.tamaño, self.nombre,self.cuerdas, self.tipo, self.color))

	def TipoGuitarra(self):
		preg=input('¿La guitarra es electrica?')
		if preg== 'si':
			print('La guitarra electrica puede ser marca Parker, Cort, Yamaha, Dean, ESP')

	def Afinar(self):

		print('La guitarra fue afinada')



class Bateria(Instrumento_musical):
	def __init__(self,clasificacion,tamaño,nombre,platillos='', bombo='',baquetas=''):
		Instrumento_musical.__init__(self,clasificacion,tamaño,nombre)
		self.platillos=platillos
		self.bombo=bombo
		self.baquetas=baquetas
	def __str__(self):
		return('\n Batería:\n de clasificacion: {} \n tamaño: {} \n nombre: {} \n tipo de platillos: {} \n tamaño de bombo: {} \n material de baquetas: {}'.format(self.clasificacion, self.tamaño, self.nombre,self.platillos, self.bombo, self.baquetas))

	def TipoBaqueta(self):
		preg=input('¿que tipo de baquetas te gusta; pesadas o ligeras?')
		if preg=='ligeras':
			print('Estas baquetas se usan para estilos más suaves Jazz o Pop ')
		else :
			print('Estas baquetas se usan para estilos mas contundentes como Hard Rock y Metal')

	def PrecioBateria(self):
		print('')

		preg=input('¿Cuántas piezas tiene la batería?')
		precio= preg * 478
		print('El precio de esta bateria es: '+ precio)


g=Guitarra("cuerda","mediana","Guitarra","6","electrica", "negra")
print (g)
g=Guitarra("cuerda","grande","Guitarra","7","acustica", "rosa")
print (g)
g=Guitarra("cuerda","chica","Guitarra","8","electroacustica", "gris")
print (g)


b=Bateria("percusion","grande","Bateria","crash","18","madera")
print(b)
b=Bateria("percusion","grande","Bateria","ride","19","fibra")
print(b)
b=Bateria("percusion","grande","Bateria","Hi-hats","20","aluminio")
print(b)