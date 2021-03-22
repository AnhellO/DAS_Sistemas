from abc import ABCMeta, abstractclassmethod

class Cajero(metaclass=ABCMeta):
    #Interfaz
    @abstractclassmethod
    def next_succesor(succesor):
        pass

    @abstractclassmethod
    def handle(cantidad):
        pass

class Cajero50(Cajero):
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

class Cajero20(Cajero):
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

class Cajero10(Cajero):
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

class CajeroATMChain:
    def __init__(self):
        self.chain1 = Cajero50()
        self.chain2 = Cajero20()
        self.chain3 = Cajero10()

        self.chain1.next_succesor(self.chain2)
        self.chain2.next_succesor(self.chain3)

if __name__ == '__main__':
    ATM = CajeroATMChain()
    cantidad = int(input("que cantidad desea sacar?: "))
    if cantidad < 10 or cantidad % 10 != 0:
        print("saldo insuficiente")
        exit()
    ATM.chain1.handle(cantidad)
    print(f"la cantidad de {cantidad} fue entregada...")
    print("que tenga un buen dia...")
