import unittest

from simple import *

class BuilderTest(unittest.TestCase):
    def test_mujer_25_sfuerza_vlaser_kripto(self):
        builder = HeroBuilder("Mujer",25)
        builder.addSfuerza()
        builder.addVlaser()
        builder.addKripto()
        hero = builder.build()

        self.assertIsInstance(hero, Hero)
        self.assertEqual(
            'Mi Super Heroe es Mujer y tiene 25 años de edad con los siguientes poderes: super fuerza y vision laser, y su debilidad es kriptonita',
            str(hero)
        )

    def test_hombre_30_volar_Proca_Bplata(self):
        builder = HeroBuilder("Hombre",30)
        builder.addVolar()
        builder.addProca()
        builder.addBplata()
        hero = builder.build()

        self.assertIsInstance(hero, Hero)
        self.assertEqual(
            'Mi Super Heroe es Hombre y tiene 30 años de edad con los siguientes poderes: volar y piel roca, y su debilidad es balas de plata',
            str(hero)
        )

    def test_mujer_18_telapatia_svel_elec(self):
        builder = HeroBuilder("Mujer",18)
        builder.addTelepatia()
        builder.addSvel()
        builder.addElectricidad()
        hero = builder.build()

        self.assertIsInstance(hero, Hero)
        self.assertEqual(
            'Mi Super Heroe es Mujer y tiene 18 años de edad con los siguientes poderes: telepatia y super velocidad, y su debilidad es electricidad',
            str(hero)
        )
    def test_hombre_20_svel_volar_fuego(self):
        builder = HeroBuilder("Hombre",20)
        builder.addSvel()
        builder.addVolar()
        builder.addFuego()
        hero = builder.build()

        self.assertIsInstance(hero, Hero)
        self.assertEqual(
            'Mi Super Heroe es Hombre y tiene 20 años de edad con los siguientes poderes: super velocidad y volar, y su debilidad es fuego',
            str(hero)
        )

if __name__ == "__main__":
    unittest.main()