from abc import ABCMeta, abstractclassmethod

class CajeroHandler(metaclass=ABCMeta):
    #Interfaz
    @abstractclassmethod
    def next_succesor(succesor):
        pass

    @abstractclassmethod
    def handle(cantidad):
        pass

'''
Esta función lo que hace es determinar cuantos billetes de 50 se entregarán y
pasarle el resto al sucesor.
'''
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >=50:
            num = cantidad // 50
            sobrante = cantidad % 50
            print(f"entregando {num} billetes de 50")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

'''
Esta función lo que hace es determinar cuantos billetes de 20 se entregarán y
pasarle el resto al sucesor.
'''
class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >= 20:
            num = cantidad // 20
            sobrante = cantidad % 20
            print(f"entregando {num} billetes de 20")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

'''
Esta función lo que hace es determinar cuantos billetes de 10 se entregarán y
pasarle el resto al sucesor.
'''
class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >= 10:
            num = cantidad // 10
            sobrante = cantidad % 10
            print(f"entregando {num} billetes de 10")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

'''
Esta función determina cuales son los sucesores de cada cadena
'''
class CajeroATMChain:
    def __init__(self):
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()

        self.chain1.next_succesor(self.chain2)
        self.chain2.next_succesor(self.chain3)
'''
if __name__ == '__main__':
    ATM = CajeroATMChain()
    cantidad = int(input("Cuánto desea sacar?: "))
    if cantidad < 10 or cantidad % 10 != 0:
        print("nel krnal, ingresa números positivos y en múltiplos de 10")
        exit()
    ATM.chain1.handle(cantidad)
    print("Ya vete krnal, ya le llamé a la clica")
'''