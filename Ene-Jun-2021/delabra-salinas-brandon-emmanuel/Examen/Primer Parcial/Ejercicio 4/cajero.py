from abc import ABCMeta, abstractstaticmethod

# en la función next sucesor establecemos al siguiente sucesor dentro de la cadena
#la sifuiente función el evento de la cadena
class CajeroHandler(metaclass=ABCMeta):
    @abstractstaticmethod
    def next_succesor(next):
        
    @abstractstaticmethod
    def handle(cantidad):
        

#se definen las clases con las funciones de cada uno de los cajeros
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor=None

    def next_succesor(self, sucesor):
        self._sucesor = sucesor

    def handle(self, cambio):
        if cambio >= 50:
            numero = cambio // 50
            resto = cambio % 50
            print (f"Dar{numero} $50")
            if resto !=0:
                self._next.handle(resto)
        else:
            self._next.handle(cambio)


class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor=None

    def next_succesor(self, sucesor):
        self._sucesor = sucesor

    def handle(self, cambio):
        if cambio >= 20:
            numero = cambio // 20
            resto = cambio % 20
            print (f"Dar {numero} $20")
            if resto !=0:
                self._next.handle(resto)
        else:
            self._next.handle(cambio)

            

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor=None

    def next_succesor(self, sucesor):
        self._sucesor = sucesor

    def handle(self, cambio):
        if cambio >= 10:
            numero = cambio // 10
            resto = cambio % 10
            print (f" Dar{numero} $10")
            if resto !=0:
                self._next.handle(resto)
        else:
            self._next.handle(cambio)

class CajeroATMchain:
    #La instancia que indica el cambio del cliente
    self.chain1 = Cajero50ConcreteHandler()
    self.chain2 = Cajero20concretehandler()
    self.chain2 = Cajero10concretehandler()

    #se establece la consulta del cambio, ya sea por medio del cliente
    #o ya sea el mismo conttrolador 

    self.chain1.set_sucesor(self.chain2)
    self.chain2.set_sucesor(self.chain3)

if __name__ == '__main__':
    
    cajero=CajeroATMChain()
    Ingreso=int(input("Cantidad la cual va a ingrasar: "))
    if ingreso < 10 or ingreso % 10 !=0 :
         print("debes dar una cantidad multiplo de 10 ")
                
     cajero.chain1.handle(ingreso) 