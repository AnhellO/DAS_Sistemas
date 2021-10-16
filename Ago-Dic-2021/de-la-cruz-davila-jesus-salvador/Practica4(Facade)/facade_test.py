import unittest

from facade import *

class FacadeTest(unittest.TestCase):

    def test_lavado_camisa(self):
        lavado = Lavado()
        resultado = lavado.lavando(prendas['camisa'])
        self.assertEqual("Prendiendo Lavadora\nPreparando Lavadora\nLavando....\nTiempo de lavado: 1", resultado)

    def test_enjuagado_camisa(self):
        enjuague = Enjuague()
        resultado = enjuague.enjuagando(prendas['camisa'])
        self.assertEqual("Deteniendo Lavadora\nLavadora Detenida\nEnjuagando......\nTiempo de enjuague: 1", resultado)

    def test_todos_los_servicios_a_una_sola_prenda(self):
        lavado = Lavado()
        enjuague = Enjuague()
        secado = Secar()
        resultado = lavado.lavando(prendas['camisa'])
        resultado2 = enjuague.enjuagando(prendas['camisa'])
        resultado3 = secado.secando(prendas['camisa'])
        resultado_final = resultado + "\n" + resultado2  + "\n"+ resultado3
        self.assertEqual(
            "Prendiendo Lavadora\nPreparando Lavadora\nLavando....\nTiempo de lavado: 1\nDeteniendo Lavadora\nLavadora Detenida\nEnjuagando......\nTiempo de enjuague: 1\nPreparando modo Secado\nSecando....\nTiempo de secado: 1"
            , resultado_final)

    def test_un_servicio_para_cada_prenda(self):
        lavado = Lavado()
        enjuague = Enjuague()
        secado = Secar()
        resultado = lavado.lavando(prendas['camisa'])
        resultado2 = enjuague.enjuagando(prendas['pantalon'])
        resultado3 = secado.secando(prendas['saco'])
        resultado_final = resultado + "\n" + resultado2  + "\n"+ resultado3
        self.assertEqual(
            "Prendiendo Lavadora\nPreparando Lavadora\nLavando....\nTiempo de lavado: 1\nDeteniendo Lavadora\nLavadora Detenida\nEnjuagando......\nTiempo de enjuague: 2\nPreparando modo Secado\nSecando....\nTiempo de secado: 4"
            , resultado_final)

    def test_ninguna_prenda_elegida_y_ni_un_servicio(self):
        resultado_final = ""
        self.assertEqual("", resultado_final)

if __name__ == '__main__':
    unittest.main()