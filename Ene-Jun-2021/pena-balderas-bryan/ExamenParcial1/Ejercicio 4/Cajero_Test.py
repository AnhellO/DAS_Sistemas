import unittest

from Cajero import *


class DecoratorTest(unittest.TestCase):
    def test_principal(self):
        dinero=220
        handler_1=Cajero50ConcreteHandler()
        handler_2=Cajero20ConcreteHandler()
        handler_3=Cajero10ConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual(handler_1.handle(dinero)," se usaron 4 de 50  se usaron 1 de 20 ")

    def test_todos(self):
        dinero=530
        handler_1=Cajero50ConcreteHandler()
        handler_2=Cajero20ConcreteHandler()
        handler_3=Cajero10ConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual(handler_1.handle(dinero)," se usaron 10 de 50  se usaron 1 de 20  se usaron 1 de 10 ")


if __name__=="__main__":
    unittest.main()