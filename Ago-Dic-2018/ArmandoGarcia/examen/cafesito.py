import abc

#Clase Abstracta de Café estructura
class Abstract_Coffee(metaclass=abc.ABCMeta):

   def get_precio(self):
      pass

   def get_ingredients(self):
      pass

#Tipo de Café que implementa la clase abstacta Café
class CafeSimple(Abstract_Coffee):

   def get_precio(self):
      return 25.00

   def get_ingredients(self):
      return 'Simple'

#Clase Abstracta de Decorador, implementa la clase abstracta de Café,todos los ingredientes
class Abstract_Coffee_Decorator(Abstract_Coffee,metaclass=abc.ABCMeta):

   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee

   def get_precio(self):
      return self.decorated_coffee.get_precio()

   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients()

#Tipo de Decorador(en este caso ingrediente), implementa la clase abtsracta de Decorador de arriba (Abstract_Coffee_Decorator)
class Azucar(Abstract_Coffee_Decorator):

   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

   def get_precio(self):
      return self.decorated_coffee.get_precio()

   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', azucar'


class Canela(Abstract_Coffee_Decorator):

   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

   def get_precio(self):
      return self.decorated_coffee.get_precio() + 5.00

   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', Canela'

class Leche(Abstract_Coffee_Decorator):

   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

   def get_precio(self):
      return self.decorated_coffee.get_precio() + 3.00

   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', leche'


class Vainilla(Abstract_Coffee_Decorator):

   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

   def get_precio(self):
      return self.decorated_coffee.get_precio() + 7.00

   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', vainilla'



if __name__ == "__main__":
    #Aqui no usas decoradores,solo creas el objeto normal y ves sus caracteristicas
    cafe = CafeSimple()
    print('ingredientes: '+cafe.get_ingredients()+
       '; precio: '+str(cafe.get_precio()))

    #Se crea un Café Simple con leche, vainilla y azucar
    #Aqui "Decoras" el objeto llamando funcion dentro de otra funcion para ir agregando decoradores
    # Despues imprimes sus ingredientes y precio
    cafecito = Leche(CafeSimple())
    print('ingredientes: '+cafecito.get_ingredients()+
       '; precio: '+str(cafecito.get_precio()))

    cafecito2 = Canela(Leche(CafeSimple()))
    print('ingredientes: '+cafecito2.get_ingredients()+
       '; precio: '+str(cafecito2.get_precio()))

    cafecito3 = Canela(CafeSimple())
    print('ingredientes: '+cafecito3.get_ingredients()+
       '; precio: '+str(cafecito3.get_precio()))

    cafecito4 = Vainilla(CafeSimple())
    print('ingredientes: '+cafecito4.get_ingredients()+
       '; precio: '+str(cafecito4.get_precio()))
