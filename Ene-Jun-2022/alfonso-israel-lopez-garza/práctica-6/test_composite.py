from lib2to3.pytree import Leaf
import unittest
import composite 

class TestComposite(unittest.TestCase):
    def test_leaf(self):
        casos = [
            ("/Archivo:ejemplo1", "ejemplo1"),
            ("/Archivo:texto.txt","texto.txt"),
            ("/Archivo:imagen.png","imagen.png")
        ]

        for esperado, entrada in casos:
            with self.subTest(esperado = esperado, entrada = entrada):
                obtenido = composite.leaf(entrada)
                self.assertEqual(esperado, obtenido.imprimeEstructura())

    def test_composite(self):
        casos = [
            ("/Directorio/Directorio/Archivo:imagen.png","C","Escritorio","imagen.png"),
        ]

        for esperado, a, b, c in casos:
            with self.subTest(esperado = esperado, a = a, b = b, c = c):
                tree = composite.Composite(a)
                directorio = composite.Composite(b)
                directorio.add(composite.leaf(c))
                tree.add(directorio)
                self.assertEqual(esperado, tree.imprimeEstructura())


if __name__== "__main__":
    unittest.main()