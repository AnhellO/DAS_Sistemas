from abc import ABCMeta, abstractstaticmethod

#mi Handler
class CajeroHandler(metaclass=ABCMeta):
    @abstractstaticmethod
    def next_succesor(next):
        """siguiente handler en la cadena"""
    @abstractstaticmethod
    def handle(cantidad):
        """lo que ocurre"""

#mis handlers concretos 
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next=None
    def next_succesor(self, next):
        self._next = next
    def handle(self, cantidad):
        if cantidad >= 50:
            num=cantidad // 50
            r=cantidad % 50
            print(f"Dar {num} de 50")
            if r !=0:
                self._next.handle(r)
        else:
            self._next.handle(cantidad)

class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next=None
    def next_succesor(self, next):
        self._next = next
    def handle(self, cantidad):
        if cantidad >= 20:
            num=cantidad // 20
            r=cantidad % 20
            print(f"Dar {num} de 20")
            if r !=0:
                self._next.handle(r)
        else:
            self._next.handle(cantidad)

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next=None
    def next_succesor(self, next):
        self._next = next
    def handle(self, cantidad):
        if cantidad >= 10:
            num=cantidad // 10
            r=cantidad % 10
            print (f"Dar {num} de 10")
            if r !=0:
                self._next.handle(r)
        else:
            self._next.handle(cantidad)

#donde creo mis instancias
class CajeroATMChain:
    def __init__(self):
        self.chain1=Cajero50ConcreteHandler()
        self.chain2=Cajero20ConcreteHandler()
        self.chain3=Cajero10ConcreteHandler()
        self.chain1.next_succesor(self.chain2)
        self.chain2.next_succesor(self.chain3)

# if __name__ == '__main__':
#     cajero=CajeroATMChain()
#     dinero=int(input("Cantidad: "))
#     if dinero < 10 or dinero % 10 !=0 :
#         print("debes dar una cantidad multiplo de 10 ")
#         exit()
#     cajero.chain1.handle(dinero)