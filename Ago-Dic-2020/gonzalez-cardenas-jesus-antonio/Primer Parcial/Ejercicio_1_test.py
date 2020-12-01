import unittest
from Ejercicio_1 import *

class playertest(unittest.TestCase):
    def test_add_track(self):
        music_list = []
        music_list_test = []
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        track1 = Pista("Come together", True, "4:19", "The Beatles")
        music_list_test.append(track1)
        music_plyr.add_pista(track1)
        self.assertEqual(music_plyr.track_list,music_list_test)
    
    def test_delete_track(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        track2 = Pista("Something", True, "3:02", "The Beatles")
        track3 = Pista("Maxwell's Silver Hammer", False, "3:27", "The Beatles")
        track4 = Pista("Oh! Darling", False, "3:27", "The Beatles")
        track5 = Pista("Octopus Garden", True, "2:51", "The Beatles")
        music_list = []
        music_list.append(track1)
        music_list.append(track2)
        music_list.append(track3)
        music_list.append(track4)
        music_list.append(track5)
        music_list_test = music_list
        music_list_test.remove(track3)
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        music_plyr.remove_pista(track3)
        self.assertEqual(music_plyr.track_list,music_list_test)

    def test_add_genre(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        track1.add_genre("rock")
        self.assertEqual(track1.get_nombre(), "Come together - rock")

    def test_fail_remove(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        track2 = Pista("Something", True, "3:02", "The Beatles")
        track3 = Pista("Maxwell's Silver Hammer", False, "3:27", "The Beatles")
        track4 = Pista("Oh! Darling", False, "3:27", "The Beatles")
        track5 = Pista("Octopus Garden", True, "2:51", "The Beatles")
        trackx = Pista("Paint it, Black", True, "3:47", "The Rolling Stones")
        music_list = []
        music_list.append(track1)
        music_list.append(track2)
        music_list.append(track3)
        music_list.append(track4)
        music_list.append(track5)
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        self.assertEqual(music_plyr.remove_pista(trackx),"No se puede borrar ese track, no esta en la playlist")

    def test_get_player_info(self):
        music_list = []
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        self.assertEqual(music_plyr.name,"Python Player")

    def test_get_player_version(self):
        music_list = []
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        self.assertEqual(music_plyr.version,"1.0")

    def test_starred_music_list(self):
        music_list = []
        music_list_starred = []
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        track2 = Pista("Something", True, "3:02", "The Beatles")
        track3 = Pista("Maxwell's Silver Hammer", False, "3:27", "The Beatles")
        track4 = Pista("Oh! Darling", False, "3:27", "The Beatles")
        track5 = Pista("Octopus Garden", True, "2:51", "The Beatles")
        trackx = Pista("Paint it, Black", True, "3:47", "The Rolling Stones")
        music_list.append(track1)
        music_list.append(track2)
        music_list.append(track3)
        music_list.append(track4)
        music_list.append(track5)
        music_list.append(trackx)
        music_list_starred.append(track2)
        music_list_starred.append(track5)
        music_list_starred.append(trackx)
        music_plyr = ReproductorMusical("Python Player", music_list, "1.0")
        self.assertEqual(music_plyr.get_starred_tracks(),music_list_starred)

    def test_get_review(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        review = track1.get_review()
        self.assertIsNotNone(review)

    def test_get_track_info(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        self.assertEqual(track1.get_nombre(), "Come together")
        self.assertEqual(track1.get_artist(), "The Beatles")
        self.assertEqual(track1.get_lenght(), "4:19")

    def test_mod_track(self):
        track1 = Pista("Come together", False, "4:19", "The Beatles")
        track1.set_nombre("Paint it, Black")
        track1.set_artist("Rolling Stones")
        track1.set_lenght("3:47")
        self.assertEqual(track1.get_nombre(), "Paint it, Black")
        self.assertEqual(track1.get_artist(), "Rolling Stones")
        self.assertEqual(track1.get_lenght(), "3:47")
    
    
    




    

if __name__ == "__main__":
    unittest.main()