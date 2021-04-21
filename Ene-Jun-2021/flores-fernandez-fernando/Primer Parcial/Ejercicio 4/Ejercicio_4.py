import abc
class CajeroHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def next_succesor(CajeroHandler):
        pass
    @abc.abstractmethod
    def handle(cantidad):
        pass

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self): 
        self._next = None
        
    def next_succesor(self,CajeroHandler):
        self._next = CajeroHandler 
        
    def handle(self, cantidad):
        if (cantidad >= 10):
            num = cantidad // 10
            remainder = cantidad % 10
            print(f"Dispensando {num} billetes de $10")
            if (remainder != 0):
                self._next.handle(remainder)
        else:
            self._next.handle(cantidad)

class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self): 
        self._next = None
        
    def next_succesor(self,CajeroHandler):
        self._next = CajeroHandler 
        
    def handle(self, cantidad):
        if (cantidad >= 20):
            num = cantidad // 20
            remainder = cantidad % 20
            print(f"Dispensando {num} billetes de $20")
            if (remainder != 0):
                self._next.handle(remainder)
        else:
            self._next.handle(cantidad)

class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self): 
        self._next = None
        
    def next_succesor(self,CajeroHandler):
        self._next = CajeroHandler 
        
    def handle(self, cantidad):
        if (cantidad >= 50):
            num = cantidad // 50
            remainder = cantidad % 50
            print(f"Dispensando {num} billetes de $50")
            if (remainder != 0):
                self._next.handle(remainder)
        else:
            self._next.handle(cantidad)
                
class CajeroATMChain:
    
    def __init__(self):
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()
            
        self.chain1.next_succesor(self.chain2)
        self.chain2.next_succesor(self.chain3)
        

def main():
    ATM = CajeroATMChain()
    ATM.chain1.handle(130)

if __name__ == '__main__':
    main()   