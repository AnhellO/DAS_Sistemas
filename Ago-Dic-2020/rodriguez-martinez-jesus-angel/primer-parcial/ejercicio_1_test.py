import unittest
from ejercicio_1 import *

class PistaTest(unittest.TestCase):
    def test_stars(self):
        anime_opening = Pista('Anime opening', True, 100,'2020-01-01')
        anime_opening.add_star()
        anime_opening.add_star()
        anime_opening.add_star()
        self.assertEqual("Stars: ★★★", anime_opening.get_stars())
    def test_favorite_song(self):
        anime_ending = Pista('Anime ending', True, 100,'2020-01-01')
        self.assertEqual("This is one of your favorite songs", anime_ending.is_favorite())
    def test_not_a_favorite_song(self):
        anime_ending = Pista('Anime ending', False, 100,'2020-01-01')
        self.assertEqual("This is not one of your favorite songs", anime_ending.is_favorite())

class ReproductorMusicalTest(unittest.TestCase):

    def test_duration(self):
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        self.assertEqual(911, reproductor.get_duration())

    def test_background(self):
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        self.assertEqual('https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', reproductor.get_background())

    def test_no_starred_songs(self):
        test_cases = [
            Pista('Naruto opening 5', False, 100,'2020-01-01'),
            Pista('Full metal alchemist brotherhood', False, 1,'2019-01-01'),
            Pista('Saint seiya lost canvas opening', False, 10,'2019-01-01'),
            Pista('Zankyou no terror ending', False, 1050,'2030-01-01')
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("", reproductor.get_favorite_songs())

    def test_remove_last_song(self):
        test_cases = [
            Pista('Naruto opening 5', True, 100,'2020-01-01'),
            Pista('Full metal alchemist brotherhood', True, 1,'2019-01-01'),
            Pista('Saint seiya lost canvas opening', True, 10,'2019-01-01'),
            Pista('Zankyou no terror ending', True, 1050,'2030-01-01')
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        reproductor.remove_last_song()
        self.assertEqual("Full metal alchemist brotherhood, Saint seiya lost canvas opening, Naruto opening 5", reproductor.get_favorite_songs())

    def test_four_songs(self):
        test_cases = [
            Pista('Naruto opening 5', True, 100,'2020-01-01'),
            Pista('Full metal alchemist brotherhood', True, 1,'2019-01-01'),
            Pista('Saint seiya lost canvas opening', True, 10,'2019-01-01'),
            Pista('Zankyou no terror ending', True, 1050,'2030-01-01')
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("Full metal alchemist brotherhood, Saint seiya lost canvas opening, Naruto opening 5, Zankyou no terror ending", reproductor.get_favorite_songs())

    def test_three_songs(self):
        test_cases = [
            Pista('Naruto opening 5', True, 100,'2020-01-01'),
            Pista('Saint seiya lost canvas opening', True, 10,'2019-01-01'),
            Pista('Zankyou no terror ending', True, 1050,'2030-01-01')
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("Saint seiya lost canvas opening, Naruto opening 5, Zankyou no terror ending", reproductor.get_favorite_songs())

    def test_two_songs(self):
        test_cases = [
            Pista('Naruto opening 5', True, 100,'2020-01-01'),
            Pista('Saint seiya lost canvas opening', True, 10,'2019-01-01'),
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("Saint seiya lost canvas opening, Naruto opening 5", reproductor.get_favorite_songs())

    def test_one_songs(self):
        test_cases = [
            Pista('Naruto opening 5', True, 100,'2020-01-01'),
        ]
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("Naruto opening 5", reproductor.get_favorite_songs())

    def test_no_songs(self):
        test_cases = []
        reproductor = ReproductorMusical('Icelandic', 'https://i.ytimg.com/vi/uVFGmjzQgW4/maxresdefault.jpg', 911)
        for case in test_cases:
            reproductor.add_song(case)
        self.assertEqual("", reproductor.get_favorite_songs())

if __name__ == "__main__":
    unittest.main()