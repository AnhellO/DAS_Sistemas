import abc

class CafeAbstracto:
	def precio(self):
		pass

	def tipo(self):
		pass

class CafeSimple(CafeAbstracto):
	def precio(self):
		return 25

	def tipo(self):
		return 'Cafecito!'

class DecorandoelCafe(CafeAbstracto, metaclass=abc.ABCMeta):
	def __init__(self, decoracion):
		self.decoracion = decoracion

	def precio(self):
		return self.decoracion.precio()

	def tipo(self):
		return self.decoracion.tipo()

class Vainilla(DecorandoelCafe):
	def __init__(self, decoracion):
		DecorandoelCafe.__init__(self, decoracion)

	def precio(self):
		return self.decoracion.precio() + 7

	def tipo(self):
		return self.decoracion.tipo() + ' con Vainilla!'

class Leche(DecorandoelCafe):
	def __init__(self, decoracion):
		DecorandoelCafe.__init__(self, decoracion)

	def precio(self):
		return self.decoracion.precio() + 3

	def tipo(self):
		return self.decoracion.tipo() + ' con Leche!'

class Canela(DecorandoelCafe):
	def __init__(self, decoracion):
		DecorandoelCafe.__init__(self, decoracion)

	def precio(self):
		return self.decoracion.precio() + 5

	def tipo(self):
		return self.decoracion.tipo() + ' con Canela!'

class LecheCanela(DecorandoelCafe):
	def __init__(self, decoracion):
		DecorandoelCafe.__init__(self, decoracion)

	def precio(self):
		return self.decoracion.precio() + 8

	def tipo(self):
		return self.decoracion.tipo() + ' con Leche! con Canela!'

if __name__ == '__main__':
	cafecito = CafeSimple()
	print(cafecito.tipo())

	cafecitoDecorado = Vainilla(CafeSimple())
	print(cafecitoDecorado.tipo() + ' A solo {} pesitos'.format(cafecitoDecorado.precio()))

	cafecitoDecorado2 =Leche(CafeSimple())
	print(cafecitoDecorado2.tipo() + ' A solo {} pesitos'.format(cafecitoDecorado2.precio()))

	cafecitoDecorado3 =Canela(CafeSimple())
	print(cafecitoDecorado3.tipo() + ' A solo {} pesitos'.format(cafecitoDecorado3.precio()))

	cafecitoDecorado4 =Canela(Leche(CafeSimple()))
	print(cafecitoDecorado4.tipo() + ' A solo {} pesitos'.format(cafecitoDecorado4.precio()))


# Explica la lógica implementada detrás de tu enfoque
# Primero se creaba una clase que tuviera los atributos basicos de un cafe, que recibiría los parametros para despues mandarselos a la otra clase que especifíca un tipo de cafe base
# Esta clase base sin decorar es la que tiene los atributos definidos
# Enseguida se creó otra clase que será la que se implemente en los decoradores o en este caso ingrediientes con los que queremos decorar el cafe
# Esta clase contiene las funciones que cada ingrediente tambien lleva, pero en cada ingrediente se detalla lo que queremos especificar de ese ingrediente en específico,
# como por ejemplo se le añadió un costo extra dependiendo del ingrediente
# por ultimo en el apartado de main, donde se creará el objeto cafe, mandamos llamar primero a al ingrediente decorador que le aplicaremos al cafe simple
# despues se imprimen el resultado por medio del objeto instanciado de las clases (ingrediente decorador y cafe simple) 
