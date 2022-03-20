import unittest
from prototype import *

class Oveja_test(unittest.TestCase):

    def test_clase_oveja(self):
        oveja = OvejaConcretePrototype('Dolly', 'droper')
        self.assertIsInstance(oveja, OvejaConcretePrototype)
    
    def test_get_nombre(self):
        oveja = Oveja('kevin', 'castellana')
        self.assertEqual(oveja.get_nombre(),'kevin')

    def test_get_tipo(self):
        oveja = Oveja('kevin', 'castellana')
        self.assertEqual(oveja.get_tipo(),'castellana')
    
    def test_set_nombre(self):
        oveja = Oveja('kevin', 'castellana')
        oveja.set_nombre('edson')
        self.assertEqual(oveja.get_nombre(),'edson')

    def test_set_tipo(self):
        oveja = Oveja('kevin', 'castellana')
        oveja.set_tipo('merina')
        self.assertEqual(oveja.get_tipo(),'merina')

    def test_clone(self):
        oveja = OvejaConcretePrototype('Dolly', 'droper')
        oveja_clon = oveja.clone()

        self.assertEqual(oveja.get_nombre(),oveja_clon.get_nombre())
        self.assertEqual(oveja.get_tipo(),oveja_clon.get_tipo())

if __name__=="__main__":
    unittest.main()