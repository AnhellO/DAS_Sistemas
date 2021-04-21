from abc import ABCMeta, abstractclassmethod

class CajeroHandler(metaclass=ABCMeta):
    #Interfaz
    @abstractclassmethod
    def next_sucesor(sucesor):
        pass

    @abstractclassmethod
    def handle(monto):
        pass

class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor = None

    def next_sucesor(self, sucesor):
        self._sucesor = sucesor
    
    def handle(self,monto):
        if monto >=50:
            contador = monto // 50
            sobra = monto % 50
            print(f"{contador} billete(s) de 50")
            if sobra != 0:
                self._sucesor.handle(sobra)
        else:
            self._sucesor.handle(monto)

class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor = None

    def next_sucesor(self, sucesor):
        self._sucesor = sucesor
    
    def handle(self,monto):
        if monto >=20:
            contador = monto // 20
            sobra = monto % 20
            print(f"{contador} billete(s) de 20")
            if sobra != 0:
                self._sucesor.handle(sobra)
        else:
            self._sucesor.handle(monto)

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._sucesor = None

    def next_sucesor(self, sucesor):
        self._sucesor = sucesor
    
    def handle(self,monto):
        if monto >=10:
            contador = monto // 10
            sobra = monto % 10
            print(f"{contador} billete(s) de 10")
            if sobra != 0:
                self._sucesor.handle(sobra)
        else:
            self._sucesor.handle(monto)

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