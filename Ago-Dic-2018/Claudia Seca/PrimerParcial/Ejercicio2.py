import abc


# El Patrón de diseño 'Decorator' es un patrón perteneciente a la categoría de patrones estructurales

# Clase Abstracta de Cafecito
class Abstract_Cafecito(metaclass=abc.ABCMeta):

   def precio(self):
      pass

   def tipo(self):
      pass

   
#La clase cafecito implementa la clase abstracta, con su precio base
class Cafecito(Abstract_Cafecito):

   def precio(self):
      return 25

   def tipo(self):
      return 'Cafecito!'

#Clase Abstracta de Decorador, implementa la clase abstracta de Café,todos los decoradores(en este caso ingredientes) deben implementar estos metodos
class Abstract_Coffee_Decorator(Abstract_Cafecito,metaclass=abc.ABCMeta):

   def __init__(self,decorated_Cafecito):
      self.decorated_Cafecito = decorated_Cafecito

   def precio(self):
      return self.decorated_Cafecito.precio()

   def tipo(self):
      return self.decorated_Cafecito.tipo()

#Decorador, donde un cafecito lleva Vainilla implementando la clase abstracta 'Cafecito'
class Vainilla(Abstract_Coffee_Decorator):

   def __init__(self,decorated_Cafecito):
      Abstract_Coffee_Decorator.__init__(self,decorated_Cafecito)
#Al precio de un cafecito básico, le cuesta 13 pesos más por agregarle Vainilla
   def precio(self):
      return self.decorated_Cafecito.precio() + 13

   def tipo(self):
	   return self.decorated_Cafecito.tipo() + '  con Vainilla!'

#Decorador, donde un cafecito lleva Leche implementando la clase abstracta 'Cafecito'
class Leche(Abstract_Coffee_Decorator):

   def __init__(self,decorated_Cafecito):
      Abstract_Coffee_Decorator.__init__(self,decorated_Cafecito)
#Al precio de un cafecito básico, le cuesta 5 pesos más por agregarle Leche
   def precio(self):
      return self.decorated_Cafecito.precio() + 5

   def tipo(self):
      return self.decorated_Cafecito.tipo() + '  con Leche!'

#Decorador, donde un cafecito lleva Canela implementando la clase abstracta 'Cafecito'
class Canela(Abstract_Coffee_Decorator):

   def __init__(self,decorated_Cafecito):
      Abstract_Coffee_Decorator.__init__(self,decorated_Cafecito)
#Al precio de un cafecito básico, le cuesta 3 pesos más por agregarle Canela
   def precio(self):
      return self.decorated_Cafecito.precio() + 3

   def tipo(self):
      return self.decorated_Cafecito.tipo() + '  con Canela!'

if __name__ == "__main__":
    #caso0
    cafe = Cafecito()
    print(cafe.tipo()+' A solo '+str(cafe.precio())+'  pesitos!')

    #caso1
    cafecito = Vainilla(Cafecito())
    print(cafecito.tipo()+' A solo '+str(cafecito.precio())+'  pesitos!')

   #caso2
    cafecito2 = Leche(Cafecito())
    print(cafecito2.tipo()+' A solo '+str(cafecito2.precio())+' pesitos!')

    #caso3
    cafecito3 = Canela(Cafecito())
    print(cafecito3.tipo()+' A solo '+str(cafecito3.precio())+' pesitos!')
    #caso4
    cafecito4 = Leche(Canela(Cafecito()))
    print(cafecito4.tipo()+' A solo '+str(cafecito4.precio())+' pesitos!')
