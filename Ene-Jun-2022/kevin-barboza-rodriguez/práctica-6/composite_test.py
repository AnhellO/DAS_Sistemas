import unittest
from composite import ArchivoComponent, ElementoLeaf, ArchivoComposite

class ElementoLeafTest(unittest.TestCase):

    def test_crear_elementoLeaf(self):
        hoja = ElementoLeaf('kevin', 'user')
        self.assertIsInstance(hoja, ElementoLeaf)
        
    def test_get_nombre(self):
        hoja = ElementoLeaf('kevin', 'user')
        self.assertEqual(hoja.get_nombre(),'kevin')

    def test_get_tipo(self):
        hoja = ElementoLeaf('kevin', 'user')
        self.assertEqual(hoja.get_tipo(),'user')

class ArchivoCompositeTest(unittest.TestCase):
    def test_crear_archivoContendor(self):
        contenedor = ArchivoComposite()
        self.assertIsInstance(contenedor, ArchivoComposite)
    
    def test_add(self):
        contenedor = ArchivoComposite()
        hoja = ElementoLeaf('kevin', 'user')
        self.assertEqual(contenedor.add(hoja), hoja.imprimeEstructura())

    def test_remove(self):
        contenedor = ArchivoComposite()
        hoja = ElementoLeaf('kevin', 'user')
        contenedor.add(hoja)
        self.assertEqual(contenedor.remove(hoja), hoja.imprimeEstructura())

if __name__ == "__main__":
    unittest.main()