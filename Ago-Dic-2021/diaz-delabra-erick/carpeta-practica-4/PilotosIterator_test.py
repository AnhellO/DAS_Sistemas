import unittest
from PilotosIterator import *
#casos de prueba
class TestPilotosIterator(unittest.TestCase):
    def test_redbull(self):
        equipo_deseado = "Redbull" 
        pilotos(equipo_deseado) 
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Sergio Perez, Max Verstappen") #se utiliza el join para modificar el sting que vamos a mandar

    def test_mercedes(self):
        equipo_deseado = "Mercedes"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Lewis Hamilton, Valteri Bottas") 

    def test_ferrari(self):
        equipo_deseado = "Ferrari"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Charles Leclerc, Carlos Sainz")

    def test_mclaren(self):
        equipo_deseado = "McLaren"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Lando Norris, Daniel Ricciardo")

    def test_alphatauri(self):
        equipo_deseado = "AlphaTauri"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Pierre Gasly, Yuki Tsunoda")

    def test_astonmartin(self):
        equipo_deseado = "AstonMartin"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Lance Stroll, Sebastian Vettel")
    
    def test_alphine(self):
        equipo_deseado = "Alphine"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Fernando Alonso, Esteban Ocon")

    def test_haas(self):
        equipo_deseado = "Haas"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Mick Schumacher, Nikita Mazepin")

    def test_alpharomeo(self):
        equipo_deseado = "AlphaRomeo"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "Antonio Giovinazzi, Kimi Raikkonen")

    def test_williams(self):
        equipo_deseado = "Williams"
        pilotos(equipo_deseado)
        collection = ListaPilotos()
        self.assertEqual(", ".join(collection), "George Rusell, Nicholas Latifi")

    
if __name__ == "__main__":
    unittest.main()