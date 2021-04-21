from abc import ABCMeta, abstractclassmethod

class CajeroHandler(metaclass=ABCMeta):
    #Interfaz
    @abstractclassmethod
    def next_succesor(succesor):
        pass

    @abstractclassmethod
    def handle(cantidad):
        pass

class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >=50:
            num = cantidad // 50
            sobrante = cantidad % 50
            print(f"{num} billete(s) de 50")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >= 20:
            num = cantidad // 20
            sobrante = cantidad % 20
            print(f"{num} billete(s) de 20")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._succesor = None

    def next_succesor(self, succesor):
        self._succesor = succesor
    
    def handle(self,cantidad):
        if cantidad >= 10:
            num = cantidad // 10
            sobrante = cantidad % 10
            print(f"{num} billete(s) de 10")
            if sobrante != 0:
                self._succesor.handle(sobrante)
        else:
            self._succesor.handle(cantidad)

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
    cantidad = int(input("INGRESE CANTIDAD: "))
    if cantidad < 10 or cantidad % 10 != 0:
        print("LO SENTIMOS:C, FAVOR DE INGRESAR NUMEROS POSITIVOS Y MULTIPLOS DE 10 :D")
        exit()
    ATM.chain1.handle(cantidad)
    print("LO SENTIMOS NO PODEMOS ATENDERLE EN ESTOS MOMENTOS....")
'''