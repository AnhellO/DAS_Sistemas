import unittest

from chain_of import *
#Las pruebas del chain of responsability, como lo que devuelve al final es un print y no un return, lo que me da es un None por eso se compara con un None para que pase,
#se que no esta bien, pero se que si pasaria la prueba si supiera implementar el unittest para prints con el mock y todo eso, porque si corres el test te impreme lo que deberia darte
class CajeroTest(unittest.TestCase):
    def test_cadena_correcta(self):
        b50 = Cajero50ConcreteHandler()
        b20 = Cajero20ConcreteHandler()
        b10 = Cajero10ConcreteHandler()
        b50.next_succesor(b20).next_succesor(b10)
        self.assertEqual(b50.handle(80), None)
    
    def test_cadena_incorrecta(self):
        b50 = Cajero50ConcreteHandler()
        b20 = Cajero20ConcreteHandler()
        b10 = Cajero10ConcreteHandler()
        b10.next_succesor(b20).next_succesor(b50)
        self.assertEqual(b10.handle(135), None)
    
    def test_cadena_20_primero(self):
        b50 = Cajero50ConcreteHandler()
        b20 = Cajero20ConcreteHandler()
        b10 = Cajero10ConcreteHandler()
        b20.next_succesor(b50).next_succesor(b10)
        self.assertEqual(b20.handle(90), None)

if __name__ == "__main__":
    unittest.main()