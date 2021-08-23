import unittest

from Ejercicio_1 import *

class Test_Web(unittest.TestCase):
    def test_instancia(self):
        lista_paginas=PaginaWeb('https://www.youtube.com/watch?v=KegynmRGtRI&t=27s', 'Con', 'HTML', 'nose', 'Top movies 2020', 'as', 'meta')
        sitio=Website('.net','blog',lista_paginas)
        self.assertIsInstance(sitio, Website)

    def test_sitio(self):
        lista_paginas=PaginaWeb('https://www.youtube.com/watch?v=KegynmRGtRI&t=27s', 'Cona', 'HTML', '<sose>', 'Top movies 2020', 'as', 'meta')
        sitio=Website('.com','',lista_paginas)
        self.assertEqual(sitio.dominio, '.com')

if __name__ == '__main__' :
    unittest.main() 