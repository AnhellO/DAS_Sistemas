import unittest
from Builder import ItalikaBuilder, Director, Moto, Builder

class TestBuilder(unittest.TestCase):
    def test_builder(self):
        italikaBuilder = ItalikaBuilder()
        director = Director()
        director.set_builder(italikaBuilder)
        italika = director.get_moto()
        italika.especificaciones()
        actual = italika.especificaciones()
        self.assertEquals(None,actual)

if __name__ == "__main__":
    unittest.main()


