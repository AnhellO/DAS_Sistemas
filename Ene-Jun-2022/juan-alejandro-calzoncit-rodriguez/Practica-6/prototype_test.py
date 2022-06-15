import unittest, copy

from prototype import Oveja

class CalculatorTest(unittest.TestCase):
    def test_create_oveja(self):
        o = Oveja('Dolly','Oveja de granja')
        self.assertIsInstance(o, Oveja)
    
    def test_input(self):
        o = Oveja('Dolly','Oveja de granja')
        self.assertIsInstance(o.get_nombre(), str)
        self.assertIsInstance(o.get_tipo(), str)
        self.assertEqual(o.get_nombre(), 'Dolly')
        self.assertEqual(o.get_tipo(), 'Oveja de granja')
        
        o.set_nombre('Dolores')
        o.set_tipo('Oveja de montaña')
        self.assertEqual(o.get_nombre(), 'Dolores')
        self.assertEqual(o.get_tipo(), 'Oveja de montaña')
    
    def test_clone(self):
        o = Oveja('Dolly','Oveja de granja')
        clone = copy.copy(o)

        self.assertEqual(o.get_nombre(),clone.get_nombre())
        self.assertEqual(o.get_tipo(), clone.get_tipo())


if __name__ == "__main__":
    unittest.main()