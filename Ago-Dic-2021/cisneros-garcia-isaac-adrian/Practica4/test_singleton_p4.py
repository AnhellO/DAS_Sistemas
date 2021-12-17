import unittest

from singleton_p4 import *

class JefeTest(unittest.TestCase):

    def test_revisar_nombre_jefe(self):
        Jefesito = ElUnico("nombre")
        self.assertEqual(ElUnico,"Salvador Hernández Vélez")
    
    def test_revisar_puesto_jefe(self):
        Jefesito = ElUnico("puesto")
        self.assertEqual(ElUnico,"Salvador Hernández Vélez")

    def test_revisar_nombre_jefe2(self):
        Jefesito = ElUnico("nombre")
        self.asserNotEqual(ElUnico,"Juanito El Manos Largas")

    def test_revisar_puesto_jefe2(self):
        Jefesito = ElUnico("puesto")
        self.assertNotEqual(ElUnico,"Diretor de FCA")
    
    
if __name__ == "__main__":
    unittest.main()