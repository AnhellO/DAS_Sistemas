#DAS Práctica 6.2

import copy

class animal:
    
   _type = None
   _value = None

   def clone(self):
      pass

   def getType(self):
      return self._type

   def getValue(self):
      return self._value

class Oveja(animal):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo

    def get_tipo(self):
        return self.tipo
    
    def clone(self):
        return copy.copy(self)
    
Ovejas=[]
Ovejas.append(Oveja("Donny", "Comestible"))

Ovejas.append(Ovejas[0].clone())
for sheep in Ovejas:
    print(sheep.get_nombre())
    
