from music import MusicApp, Song, Gender
import unittest

class MusicTest(unittest.TestCase):
	def test_song_with_valid_gender(self):
		self.assertEqual(Song(gender=Gender.pop).gender, Gender.pop)

	def test_song_with_invalid_gender(self):
		self.assertEqual(Song(gender='rock').gender, Gender.none)

	def test_convert_song_to_mp3(self):
		self.assertEqual(Song(duration=100).to_mp3().duration, 60)

	def test_add_song_premium(self):
		app = MusicApp(True)

		for _ in range(20):
			app.add_song(Song())

		self.assertEqual(len(app.get_sorted()), 20)

	def test_add_song_free(self):
		app = MusicApp()

		for _ in range(20):
			app.add_song(Song())

		self.assertEqual(len(app.get_sorted()), 5)

	def test_number_starred_song(self):
		app = MusicApp(True)

		for k in range(20):
			app.add_song(Song(starred = not k % 2))

		self.assertEqual(len(app.get_starred_songs()), 10)

	def test_starred_song(self):
		app = MusicApp(True)

		for k in range(5):
			app.add_song(Song())

		only_song_starred = Song(starred = True)
		app.add_song(only_song_starred)

		self.assertEqual(app.get_starred_songs()[0], only_song_starred)

	def test_sorted_songs(self):
		app = MusicApp(True)

		for k in range(10):
			app.add_song(Song(duration = (10 - k)))

		self.assertEqual(
			[m.duration for m in app.get_sorted()],
			[k + 1 for k in range(10)]
		)

	def test_use_dark_mode_premium(self):
		app = MusicApp(True)
		app.use_dark_mode(True)

		self.assertTrue(app.is_dark_mode_activated())

	def test_use_dark_mode_free(self):
		app = MusicApp()
		app.use_dark_mode(True)

		self.assertFalse(app.is_dark_mode_activated())


if __name__ == "__main__":
	unittest.main()

