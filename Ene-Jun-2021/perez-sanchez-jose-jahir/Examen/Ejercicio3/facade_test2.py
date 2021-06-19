import unittest

from facade import LavadoraFacade, Lavadora
#Cree estas pruebas en unittest por que pytest no me decia nada si estaba bien o mal, solo implemente las mismas pruebas y listo
class LavadoraTest(unittest.TestCase):
    def test_ciclo_completo(self):
        self.assertEqual(LavadoraFacade().ciclo_completo(),"Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!\n")

    def test_solo_centrifugado(self):
        self.assertEqual(LavadoraFacade().solo_centrifugado(),"Centrifugando...\nFinalizado!\n")

if __name__ == "__main__":
    unittest.main()
