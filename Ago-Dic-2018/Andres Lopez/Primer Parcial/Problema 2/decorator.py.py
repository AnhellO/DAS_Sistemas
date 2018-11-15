import abc

#Clase Abstracta de Café, todos las clases de café tienen que tener esta estructura
class CafeAbstracto(metaclass=abc.ABCMeta):

   def precio(self):
      pass

   def ingredientes(self):
      pass


#Tipo de Café que implementa la clase abstacta  
class CafeSimple(CafeAbstracto):

   def precio(self):
      return 25

   def ingredientes(self):
      return 'Cafesito!'

#Clase Abstracta de Decorador para todos los decoradores o  ingredientes
class Abstracto_Cafe_Decorator(CafeAbstracto,metaclass=abc.ABCMeta):

   def __init__(self,decorated_cafe):
      self.decorated_cafe = decorated_cafe

   def precio(self):
      return self.decorated_cafe.precio()

   def ingredientes(self):
      return self.decorated_cafe.ingredientes()

#Tipo de Decorador o ingrediente implementa la clase abtsracta de Decorador 
class Canela(Abstracto_Cafe_Decorator):

   def __init__(self,decorated_cafe):
      Abstracto_Cafe_Decorator.__init__(self,decorated_cafe)

   def precio(self):
      return self.decorated_cafe.precio() + 5

   def ingredientes(self):
	   return self.decorated_cafe.ingredientes() + ', con canela!'


class Leche(Abstracto_Cafe_Decorator):

   def __init__(self,decorated_cafe):
      Abstracto_Cafe_Decorator.__init__(self,decorated_cafe)

   def precio(self):
      return self.decorated_cafe.precio() + 3

   def ingredientes(self):
      return self.decorated_cafe.ingredientes() + ', con leche!'


class Vainilla(Abstracto_Cafe_Decorator):

   def __init__(self,decorated_cafe):
      Abstracto_Cafe_Decorator.__init__(self,decorated_cafe)

   def get_cost(self):
      return self.decorated_cafe.precio() + 7

   def ingredientes(self):
      return self.decorated_cafe.ingredientes() + ', con vainilla!'


if __name__ == "__main__":
#Aqui no usas decoradores,solo creas el objeto normal y ves sus caracteristicas
    cafe = CafeSimple()
    print('ingredientes: '+cafe.ingredientes()+
       '; A solo '+str(cafe.precio()))

    cafecito =(Vainilla(CafeSimple()))
    print('ingredientes: '+cafecito.ingredientes()+
       '; A solo '+str(cafecito.precio())+ ' pesitos! ')

    cafecito =(Leche(CafeSimple()))
    print('ingredientes: '+cafecito.ingredientes()+
       '; A solo '+str(cafecito.precio())+ ' pesitos! ')

    cafecito =(Canela(CafeSimple()))
    print('ingredientes: '+cafecito.ingredientes()+
       '; A solo '+str(cafecito.precio())+ ' pesitos! ')

    cafecito = Canela(Leche(CafeSimple()))
    print('ingredientes: '+cafecito.ingredientes()+
       '; A solo '+str(cafecito.precio())+ ' pesitos! ')

    
