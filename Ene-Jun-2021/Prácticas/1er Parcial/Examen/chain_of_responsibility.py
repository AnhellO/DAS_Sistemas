from abc import ABCMeta, abstractmethod

# Cajero
class CajeroATMChain:
    def __init__(self):
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)

# Interface
class CajeroHandler(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(cantidad):
        """Handle the event"""

# Handler concreto para billetes de 50
class Cajero50ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._successor = None

    def next_successor(self, successor: CajeroHandler):
        self._successor = successor

    def handle(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Entregando {num} billete(s) de $50")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)

# Handler concreto para billetes de 20
class Cajero20ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._successor = None

    def next_successor(self, successor: CajeroHandler):
        self._successor = successor

    def handle(self, amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Entregando {num} billete(s) de $20")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)

# Handler concreto para billetes de 10
class Cajero10ConcreteHandler(CajeroHandler):
    def __init__(self):
        self._successor = None

    def next_successor(self, successor: CajeroHandler):
        self._successor = successor

    def handle(self, amount):
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Entregando {num} billete(s) de $10")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
