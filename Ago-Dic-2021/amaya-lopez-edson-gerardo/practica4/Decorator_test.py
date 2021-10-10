import unittest

from Decorator import *

class DecoratorTest(unittest.TestCase):

    def test_crear_steve_base(self):
        steve = SteveConcretComponent()
        steve_basico = steve.add_item()
        self.assertEqual(steve_basico,"Steve Basico")

    def test_steve_con_casco(self):
        steve = SteveConcretComponent()
        steve_casco =CascoConcreteDecorator(steve)
        self.assertEqual(steve_casco.add_item(),'Steve Basico con casco')

    def test_steve_con_espada(self):
        steve = SteveConcretComponent()
        steve_espada =EspadaConcreteDecorator(steve)
        self.assertEqual(steve_espada.add_item(),'Steve Basico con espada')

    def test_steve_con_espada_casco(self):
        steve = SteveConcretComponent()
        steve_espada =EspadaConcreteDecorator(steve)
        steve_supremo = CascoConcreteDecorator(steve_espada)
        self.assertEqual(steve_supremo.add_item(),'Steve Basico con espada con casco')



if __name__ == "__main__":
    unittest.main()
