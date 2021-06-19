import abc

#Interface para los manejadores
class CajeroHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def next_succesor(self, CajeroHandler):
        pass
    
    @abc.abstractmethod
    def handle(self, cantidad):
        pass

#Manejador completo
class CajeroPesosConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        return f'{cantidad} pesos'

#Manejador concreto
class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        if(cantidad % 10 == 0) and cantidad >= 10:
            return f'{cantidad // 10} x $10'
        
        if(cantidad >= 10):
            print('xd',cantidad)
            return f'{cantidad // 10} x $10\n' + self._next.handle(cantidad%10)
        
        if(cantidad < 10):
            #return 'Mínimo $10'
            return self._next.handle(cantidad%20)

#Manejador concreto
class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        if (cantidad % 20 == 0) and cantidad >= 20:
            return f'{cantidad // 20} x $20'
        
        if(cantidad >= 20): 
            return f'{cantidad // 20} x $20\n' + self._next.handle(cantidad%20)
        
        if(cantidad < 20):
            return self._next.handle(cantidad)

#Manejador concreto
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        if (cantidad % 50 == 0) and cantidad >= 50:
            return f'{cantidad // 50} x $50'
        
        #Si le pasan un monto mayor al del manejador, se cuentan los billetes necesarios de, en este caso, 
        #50 y el sobrante se pasa al siguiente manejador. :)
        if(cantidad >= 50): 
            return f'{cantidad // 50} x $50\n' + self._next.handle(cantidad%50)
        
        if(cantidad < 50):
            return self._next.handle(cantidad)

class CajeroATMChain:
    def __init__(self):
        self._chain1 = Cajero50ConcreteHandler()
        self._chain2 = Cajero20ConcreteHandler()
        self._chain3 = Cajero10ConcreteHandler()
        self._chain4 = CajeroPesosConcreteHandler()
        self._chain1.next_succesor(self._chain2)
        self._chain2.next_succesor(self._chain3)
        self._chain3.next_succesor(self._chain4)

    def start(self, value) -> str:
        return self._chain1.handle(value)

def main():
    value = int(input('Insert an amount:'))
    print(CajeroATMChain().start(value))

if __name__ == "__main__":     
    main()