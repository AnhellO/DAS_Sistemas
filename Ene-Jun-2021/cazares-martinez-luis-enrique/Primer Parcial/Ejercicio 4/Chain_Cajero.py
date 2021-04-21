from abc import ABCMeta, abstractstaticmethod

#Se crea la Interfaz CajeroHandler la cual tiene 2 metodos abstractos y estaticos
class CajeroHandler(metaclass=ABCMeta):

    @abstractstaticmethod
    def next_successor(CajeroHandler):
        pass


    @abstractstaticmethod
    def handle(cantidad):
        pass

# Se crea la clase la cual nos determina cuantos billetes de 50 nos van a dar la cual
# implementa la interfaz CajeroHandler 
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next_successor = None

    def next_successor(self, next):
        self._next_successor = next

    def handle(self, cantidad):
        if cantidad >= 50:
            num = cantidad // 50
            residuo = cantidad % 50
            print(f'Otorgando {num} $50 Pesotes')
            if residuo != 0:
                self._next_successor.handle(residuo)
        else:
            self._next_successor.handle(cantidad)

# Se implementa la misma interfaz anterior, solo que cambiando el valor de los billetes
class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next_successor = None

    def next_successor(self, next):
        self._next_successor = next

    def handle(self, cantidad):
        if cantidad >= 20:
            num = cantidad // 20
            residuo = cantidad % 20
            print(f'Otorgando {num} $20 Pesotes')
            if residuo != 0:
                self._next_successor.handle(residuo)
        else:
            self._next_successor.handle(cantidad)

# Se hace lo mimso solo se cambian los billetes
class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next_successor = None

    def next_successor(self, next):
        self._next_successor = next

    def handle(self, cantidad):
        if cantidad >= 10:
            num = cantidad // 10
            residuo = cantidad % 10
            print(f'Otorgando {num} $10 Pesotes')
            if residuo != 0:
                self._next_successor.handle(residuo)
        else:
            self._next_successor.handle(cantidad)

#Se creal la logica de cuantos billetes de cada tipo se va a recibir segun la cantidad
class CajeroATMChain:
    def __init__(self):
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)


# Se comprueba que funcione correctamente el patron establecido con anterioridad.
if __name__ == '__main__':
    ATM = CajeroATMChain()
    cantidad = int(input('Dime cuanto billete quieres sacar: '))
    if cantidad < 10 or cantidad % 10 != 0:
        print('No tenemos billetes mas chicos de 10 pide 10 o mas')
        exit()
    else:
        ATM.chain1.handle(cantidad)
        print('Recoje tu billuyo')
