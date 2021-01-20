from music import MusicAppComponent, MusicApp, Song, Gender
import threading
import time

class AlertFinishSongPlugin(MusicAppComponent):
	def __init__(self, music_app):
		self.__music_app = music_app
		self.__alert_to_finish = None
	
	def __alert(self, song):
		time.sleep(song.duration)
		print(f"== La canción {song.name} ha finalizado ==")

	def play_song(self, name):
		song = self.__music_app.play_song(name)

		if song == None:
			return None

		self.__alert_to_finish = threading.Thread(target = self.__alert, args = (song,))
		self.__alert_to_finish.start()

		return song


class ShowInfoPlugin(MusicAppComponent):
	def __init__(self, music_app):
		self.__music_app = music_app

	def play_song(self, name):
		song = self.__music_app.play_song(name)

		if song == None:
			return None

		print(f"Nombre: {song.name}\nDuración: {str(song.duration)} s\nGénero: {str(song.gender)}\n")


if __name__ == "__main__":
	music_app = MusicApp()
	music_app.add_song(Song(name="Tengo miedo", duration=2))

	plugin_app = ShowInfoPlugin(AlertFinishSongPlugin(music_app))

	plugin_app.play_song("Saludos")
	plugin_app.play_song("Tengo miedo")






