import copy

#Interface
class Prototype:

   _nombre = None
   _tipo = None

   def clone(self):
      pass

   def getNombre(self):
      return self._nombre

   def getTipo(self):
      return self._tipo
  
  

#Concret Prototype
class Oveja1(Prototype):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def clone(self):
      return copy.copy(self)


#client
def main():
    Dolly = Oveja1("Damian","3")
    print(f"Aveja1\n\tnombre: {Dolly.get_nombre()}\n\ttipo: {Dolly.get_tipo()}")
    print("")
    
    Dolly2 = Dolly.clone()
    #Dolly2.set_nombre("Damian")
    Dolly2.set_tipo("8")
    print(f"Oveja2\n\tnombre: {Dolly2.get_nombre()}\n\ttipo: {Dolly2.get_tipo()}")

if __name__ == "__main__":
    main()