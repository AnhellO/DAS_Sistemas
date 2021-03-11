import unittest

from cajero_automatico import *

class CajeroAutomatico(unittest.TestCase):
    def test_cajero_automatico_100(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('2 x $50' ,cajero_50.handle(100))

    def test_cajero_automatico_80(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('1 x $50\n1 x $20\n1 x $10' ,cajero_50.handle(80))

    def test_cajero_automatico_90(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('1 x $50\n2 x $20' ,cajero_50.handle(90))

    def test_cajero_automatico_9(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('Mínimo $10' ,cajero_50.handle(9))

    def test_cajero_automatico_60(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('1 x $50\n1 x $10' ,cajero_50.handle(60))

    def test_cajero_automatico_400(self):
        cajero_50 = Cajero50ConcreteHandler()
        cajero_20 = Cajero20ConcreteHandler()
        cajero_10 = Cajero10ConcreteHandler()

        cajero_50.next_succesor(cajero_20)
        cajero_20.next_succesor(cajero_10)

        self.assertEqual('8 x $50' ,cajero_50.handle(400))

if __name__ == "__main__":
    unittest.main()