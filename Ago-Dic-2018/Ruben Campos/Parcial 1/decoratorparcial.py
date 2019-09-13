import abc
#Usamos decoradores para agregar funcionalidades al objeto en tiempo de ejecucion,"envolviendo al objeto" de decoradores
#@Clase Abstracta de Café, todos las clases de café deben tener esta estructura
class Abstracta_Café(metaclass=abc.ABCMeta):

   def precio(self):
      pass

   def tipo(self):
      pass

#Tipo de Café que implementa la clase abstacta Café de arriba (Abstract_Coffee)
class Cafecito(Abstracta_Café):

   def precio(self):
      return 25.00

   def tipo(self):
      return 'Cafecito!!'

#Clase Abstracta de Decorador, implementa la clase abstracta de Café,todos los decoradores(en este caso ingredientes) deben implementar estos metodos
class Abstracta_Decorador(Abstracta_Café,metaclass=abc.ABCMeta):

   def __init__(self,cafedecorado):
      self.cafedecorado = cafedecorado

   def precio(self):
      return self.cafedecorado.precio()

   def tipo(self):
      return self.cafedecorado.tipo()

#Tipo de Decorador(en este caso ingrediente), implementa la clase abtsracta de Decorador de arriba (Abstract_Coffee_Decorator)
class Canela(Abstracta_Decorador):

   def __init__(self,cafedecorado):
      Abstracta_Decorador.__init__(self,cafedecorado)

   def precio(self):
      return self.cafedecorado.precio() + 3.00

   def tipo(self):
	   return self.cafedecorado.tipo() + ' con canela!'

#Tipo de Decorador(en este caso ingrediente), implementa la clase abstracta de Decorador de arriba (Abstract_Coffee_Decorator)
class Leche(Abstracta_Decorador):

   def __init__(self,cafedecorado):
      Abstracta_Decorador.__init__(self,cafedecorado)

   def precio(self):
      return self.cafedecorado.precio() + 4.00

   def tipo(self):
      return self.cafedecorado.tipo() + ' con leche!'

#Tipo de Decorador(en este caso ingrediente), implementa la clase abstracta de Decorador de arriba (Abstract_Coffee_Decorator)
class Vainilla(Abstracta_Decorador):

   def __init__(self,cafedecorado):
      Abstracta_Decorador.__init__(self,cafedecorado)

   def precio(self):
      return self.cafedecorado.precio() + 5.00

   def tipo(self):
      return self.cafedecorado.tipo() + ' con vainilla!'

if __name__ == "__main__":
    #Aqui no usas decoradores,solo creas el objeto normal y ves sus caracteristicas
    cafecito = Cafecito()
    print('Ordenaste: '+cafecito.tipo()+'  Por solo: '+str(cafecito.precio())+ ' Pesitos!!' )

    #Se crea un cafe capuccino con vainilla
    #Aqui "Decoras" el objeto llamando funcion dentro de otra funcion para ir agregando decoradores
    # Despues imprimes sus ingredientes, costo e impuestos llamando sus metodos
    cafecito2 = Vainilla(Cafecito())
    print('Ordenaste: '+cafecito2.tipo()+'  Por solo: '+str(cafecito2.precio()) + ' Pesitos!!')

    #Se crea un cafe capuccino con leche
    #Aqui "Decoras" el objeto llamando funcion dentro de otra funcion para ir agregando decoradores
    # Despues imprimes sus ingredientes, costo e impuestos llamando sus metodos
    cafecito3 = Leche(Cafecito())
    print('Ordenaste: '+cafecito3.tipo()+'  Por solo: '+str(cafecito3.precio()) + ' Pesitos!!')

    #Se crea un cafe capuccino con Canela
    #Aqui "Decoras" el objeto llamando funcion dentro de otra funcion para ir agregando decoradores
    # Despues imprimes sus ingredientes, costo e impuestos llamando sus metodos
    cafecito4 = Canela(Cafecito())
    print('Ordenaste: '+cafecito4.tipo()+'  Por solo: '+str(cafecito4.precio()) + ' Pesitos!!')

    #Se crea un cafe capuccino con leche y canela
    #Aqui "Decoras" el objeto llamando funcion dentro de otra funcion para ir agregando decoradores
    # Despues imprimes sus ingredientes, costo e impuestos llamando sus metodos
    cafecito4 = Canela(Leche(Cafecito()))
    print('Ordenaste: '+cafecito4.tipo()+'  Por solo: '+str(cafecito4.precio()) + ' Pesitos!!')
