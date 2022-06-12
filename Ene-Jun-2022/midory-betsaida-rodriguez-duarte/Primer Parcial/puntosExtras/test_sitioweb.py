import unittest

from Ejercicio1 import *

class Test_SitioWeb(unittest.TestCase):
    def test_instancia(self):
        lista_paginas=[PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top movies 2020', 'slug', 'meta'),PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2020', 'slug', 'meta'),PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top animes 2020', 'slug', 'meta')]
        sitio=SitioWeb('.net','blog', "data", "data", "data", "data", "data", "data", "data", "data",lista_paginas)
        self.assertIsInstance(sitio, SitioWeb)
        
    def test_sitio(self):
        lista_paginas=[PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top movies 2020', 'slug', 'meta'),PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2020', 'slug', 'meta'),PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top animes 2020', 'slug', 'meta')]
        sitio=SitioWeb('.com','blog', "name", "name", "name", "name", "name", "name", "name", "name",lista_paginas)
        self.assertEqual(sitio.dominio, '.com')

if __name__ == '__main__' :
    unittest.main()