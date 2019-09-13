import abc
class CafeAbstracto(metaclass=abc.ABCMeta):

   def precio(self):
      pass

   def tipo(self):
      pass

class CafeSimple(CafeAbstracto):

   def precio(self):
      return 25

   def tipo(self):
      return "Cafecito!"

class AbstractaDecoradorCafe (CafeAbstracto,metaclass=abc.ABCMeta):

   def __init__(self,cafe_decorador):
      self.cafe_decorador = cafe_decorador

   def precio(self):
      return self.cafe_decorador.precio()

   def tipo(self):
      return self.cafe_decorador.tipo()

class Leche(AbstractaDecoradorCafe):

   def __init__(self,cafe_decorador):
      AbstractaDecoradorCafe.__init__(self,cafe_decorador)

   def precio(self):
      return self.cafe_decorador.precio() + 3

   def tipo(self):
      return self.cafe_decorador.tipo() + " con Leche!"

class Vainilla(AbstractaDecoradorCafe):

   def __init__(self,cafe_decorador):
      AbstractaDecoradorCafe.__init__(self,cafe_decorador)

   def precio(self):
      return self.cafe_decorador.precio() + 7

   def tipo(self):
      return self.cafe_decorador.tipo() + " con Vainilla!"

class Canela(AbstractaDecoradorCafe):

   def __init__(self,cafe_decorador):
      AbstractaDecoradorCafe.__init__(self,cafe_decorador)

   def precio(self):
      return self.cafe_decorador.precio() + 5

   def tipo(self):
	return self.cafe_decorador.tipo() + " con Canela!"

if __name__ == "__main__":

        tazadecafe1 = Vainilla(CafeSimple())
        print(tazadecafe1.tipo()+ " A solo: "+str(tazadecafe1.precio()) + " pesitos!")

        tazadecafe2 = Leche(CafeSimple())
        print(tazadecafe2.tipo()+ " A solo: "+str(tazadecafe2.precio()) + " pesitos!")

        tazadecafe3 = Canela(CafeSimple())
        print(tazadecafe3.tipo()+ " A solo: "+str(tazadecafe3.precio()) + " pesitos!")

        tazadecafe4 = Leche(Canela(CafeSimple()))
        print(tazadecafe4.tipo()+ " A solo: "+str(tazadecafe4.precio()) + " pesitos!")

        tazadecafe5 = Vainilla(Leche(CafeSimple()))
        print(tazadecafe5.tipo()+ " A solo: "+str(tazadecafe5.precio()) + " pesitos!")

        tazadecafe6 = Canela(Vainilla(CafeSimple()))
        print(tazadecafe6.tipo()+ " A solo: "+str(tazadecafe6.precio()) + " pesitos!")

#En la clase CafeAbstracto se declara como def el precio y tipo,
#ya que son los que se solicitan. La clase de CafeSimple se declaran return donde en precio
#se puede poner un precio base (puse 25) y un return donde te regrese que es, o sea Cafecito!
#La clase AbstractaDecoradorCafe implementa la clase CafeAbstracto junto con los decoradores
#(o sea la leche, vainilla y cafe)
#Se crean los calculos necesarios para cada decorador, o sea cada decorador
#se implementara con la clase AbstractaDecoradorCafe y se solicitara return para los precios
#y tipos de cafe
#Despues, para el primer cafe (ya en la parte de print)se agrega el sabor que segun se
#solicite o ingrediente que quieras agregar (canela, leche y/o vainilla) junto con el 
#precio y algunos textos extras. En si, se decora el objeto  (en este caso cada taza
#de cafe), llamando una funcion dentro de otra funcion para ir agregando decoradores y asi
#crear una funcion. Y ya al final se imprime el cafe con su respectivo sabor o ingredente y
#su precio. Basicamente mismo procedimiento para cada taza de cafe