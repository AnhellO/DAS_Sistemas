from abc import ABCMeta, abstractmethod

    #Interface handler de la que heredan todos los de mas Handlers
class CajeroHandler(metaclass=ABCMeta):

    #Se implementa el sucesor siguiente para la cadena
    def next_succesor(self, next=None): 
        self._next = next

    #metodo abstracto handle principal
    @abstractmethod
    def handle(self, cantidad):
        pass

    #Handler que maneja el cambio de billetes de $50
class Cajero50ConcreteHandler(CajeroHandler):

    # Constructor _next para pasar al siguiente
    def __init__(self):
        self._next = None

    # Se implementa el set_next para la cadena de responsabilidad
    def set_next(self, next):
        self._next = next

     # Funcion handle para crear la logica del calculo de 
     # La cantidad de billetes 
    def handle(self, cantidad):

        if cantidad >= 50:
            num = cantidad // 50
            guardar = cantidad % 50
            print(f"Cambio: {num} billetes de $50")
            if guardar != 0:
                self._next.handle(guardar)
        else:
            self._next.handle(cantidad)

    #Handler que maneja el cambio de billetes de $20
class Cajero20ConcreteHandler(CajeroHandler):

    # Constructor _next para pasar al siguiente
    def __init__(self):
        self._next = None
    
    #Se implementa el set_next para la cadena de responsabilidad
    def set_next(self, next):
        self._next = next

     # Funcion handle para crear la logica del calculo de 
     # La cantidad de billetes
    def handle(self, cantidad):

        if cantidad >= 20:
            num = cantidad // 20
            guardar = cantidad % 20
            print(f"Cambio: {num} billetes de $20")
            if guardar != 0:
                self._next.handle(guardar)
        else:
            self._next.handle(cantidad)

class Cajero10ConcreteHandler(CajeroHandler):

    # Constructor _next para pasar al siguiente
    def __init__(self):
        self._next = None

    #Se implementa el set_next para la cadena de responsabilidad en el cajero
    def set_next(self, next):
        self._next = next

     # Funcion handle para crear la logica del calculo de 
     # La cantidad de billetes
    def handle(self, cantidad):

        if cantidad >= 10:
            num = cantidad // 10
            guardar = cantidad % 10
            print(f"Cambio: {num} billetes de $10")
            if guardar != 0:
                self._next.handle(guardar)
        else:
            self._next.handle(cantidad)

    # Clase cajero para implementar la cadena de responsabilidad 
class CajeroATMChain:

    def __init__(self):
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()

        self.chain1.set_next(self.chain2)
        self.chain2.set_next(self.chain3)

    # Funcion main para crear el objeto CajeroATMChain y pasarle
    # Parametros de cantidad de dinero a las clases
def main():
    ATM1 = CajeroATMChain()

     
    #cant = 150
    #cant = 120
    cant = 130
    #cant = int(1550)

    # Ya que estamos trabajando con numeros que son multplilos de 10
    # Hay que ingresarle solo esos numeros, de otra forma, lanza el mensaje
    # Y el programa termina.
    if cant < 10 or cant % 10 != 0:
        print("Ingresa numeros positivos y que sean multiplos de 10")
        exit()
    ATM1.chain1.handle(cant)
     
  
if __name__ == "__main__":
    main()
    
