#import six
from abc import ABCMeta

#@six.add_metaclass(ABCMeta)
class CafeAbstracto(object):

   def precio(self):
      pass

   def tipo(self):
      pass
   
class CafeSimple(CafeAbstracto):
   
   def precio(self):
      return 25
   
   def tipo(self):
      return 'Cafecito'

class CafeAbstracto_Decorator(CafeAbstracto):
   
   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee
   
   def precio(self):
      return self.decorated_coffee.precio()
   
   def tipo(self):
      return self.decorated_coffee.tipo()

class Simple(CafeAbstracto_Decorator):
   
   def __init__(self,decorated_coffee):
      CafeAbstracto_Decorator.__init__(self,decorated_coffee)
   
   def precio(self):
      return self.decorated_coffee.precio()
   
   def tipo(self):
	   return self.decorated_coffee.tipo() 

class Vainilla(CafeAbstracto_Decorator):
   
   def __init__(self,decorated_coffee):
      CafeAbstracto_Decorator.__init__(self,decorated_coffee)
   
   def precio(self):
      return self.decorated_coffee.precio() + 7
   
   def tipo(self):
      return self.decorated_coffee.tipo() + ', Con vainilla!'
class Leche(CafeAbstracto_Decorator):
   
   def __init__(self,decorated_coffee):
      CafeAbstracto_Decorator.__init__(self,decorated_coffee)
   
   def precio(self):
      return self.decorated_coffee.precio() + 3
   
   def tipo(self):
      return self.decorated_coffee.tipo() + ', con Leche!'

class Canela(CafeAbstracto_Decorator):
   
   def __init__(self,decorated_coffee):
      CafeAbstracto_Decorator.__init__(self,decorated_coffee)
   
   def precio(self):
      return self.decorated_coffee.precio() + 5
   
   def tipo(self):
      return self.decorated_coffee.tipo() + ', con Canela!'

class LecheCanela(CafeAbstracto_Decorator):
   
   def __init__(self,decorated_coffee):
      CafeAbstracto_Decorator.__init__(self,decorated_coffee)
   
   def precio(self):
      return self.decorated_coffee.precio() + 8
   
   def tipo(self):
      return self.decorated_coffee.tipo() + ', con Leche! con Canela!'