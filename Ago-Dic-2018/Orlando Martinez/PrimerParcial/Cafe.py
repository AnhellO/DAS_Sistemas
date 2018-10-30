import abc
class CafeAbstracto:
	def get_precio(self):
		pass

	def get_tipo(self):
		pass

class CafeSimple(CafeAbstracto):
	def get_precio(self):
		return 25

	def get_tipo(self):
		return 'Cafecito! con'



class Decorador_Cafe_abstracto(CafeAbstracto,metaclass=abc.ABCMeta):
	def __init__(self,decorador_cafe):
		self.decorador_cafe = decorador_cafe

	def get_precio(self):
		return self.decorador_cafe.get_precio()

	def get_tipo(self):
		return self.decorador_cafe.get_tipo()


class Vainilla(Decorador_Cafe_abstracto):
	def __init__(self,decorador_cafe):
		Decorador_Cafe_abstracto.__init__(self,decorador_cafe)

	def get_precio(self):
		return self.decorador_cafe.get_precio() + 7.00


	def get_tipo(self):
		return self.decorador_cafe.get_tipo() + ' vainilla'


class Leche(Decorador_Cafe_abstracto):
	def __init__(self,decorador_cafe):
		Decorador_Cafe_abstracto.__init__(self,decorador_cafe)

	def get_precio(self):
		return self.decorador_cafe.get_precio() + 3.00

	def get_tipo(self):
   	   	return self.decorador_cafe.get_tipo() + ' Leche'

class Canela(Decorador_Cafe_abstracto):
	def __init__(self,decorador_cafe):
		Decorador_Cafe_abstracto.__init__(self,decorador_cafe)

	def get_precio(self):
		return self.decorador_cafe.get_precio() + 5.00

	def get_tipo(self):
		return self.decorador_cafe.get_tipo() + ' canela'

if __name__ == '__main__':
	cafe = Vainilla(CafeSimple())
	print(cafe.get_tipo()+
   ' a solo $'+str(cafe.get_precio()))
	cafe2 = Leche(CafeSimple())
	print(cafe2.get_tipo()+
   ' a solo $'+str(cafe2.get_precio()))

##Primero se creo la clase abstracta de cafe donde se crean las funciones de get_tipo y get_precio
##despues se creo la clase de cafe simple donde se le da el valor del cafe y el tipo de Cafe
##despues se creo la clase abstracta del decorador
##lo siguiente fue crear los decoradores para los diferentes ingredientes que se le pueden agregar al cafe
  ##y dependiendo del ingrediente se le sumo una cantidad al precio del cafe simple
