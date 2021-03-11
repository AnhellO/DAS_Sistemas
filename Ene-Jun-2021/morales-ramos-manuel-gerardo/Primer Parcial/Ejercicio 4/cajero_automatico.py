import abc

class CajeroHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def next_succesor(self, CajeroHandler):
        pass
    
    @abc.abstractmethod
    def handle(self, cantidad):
        pass

class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        if(cantidad % 10 == 0) and cantidad >= 10:
            return f'{cantidad // 10} x $10'
        
        if(cantidad >= 10):
            return f'{cantidad // 10}'
        
        if(cantidad < 10):
            return 'Mínimo $10'

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

class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._next: CajeroHandler = None

    def next_succesor(self, CajeroHandler):
        self._next = CajeroHandler

    def handle(self, cantidad):
        if (cantidad % 50 == 0) and cantidad >= 50:
            return f'{cantidad // 50} x $50'
        
        if(cantidad >= 50): 
            return f'{cantidad // 50} x $50\n' + self._next.handle(cantidad%50)
        
        if(cantidad < 50):
            return self._next.handle(cantidad)