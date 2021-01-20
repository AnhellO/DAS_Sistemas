import enum
import time
from abc import ABC, abstractmethod

class Gender(enum.Enum):
	none = 0
	rock = 1
	pop = 2
	metal = 3

class Song:
	def __init__(self, **args):
		self.name = args.get("name", "")
		self.starred = args.get("starred", False)
		self.duration = args.get("duration", 0.0)
		self.gender = args.get("gender", Gender.none)

	@property
	def gender(self):
		return self.__gender

	@gender.setter
	def gender(self, g):
		self.__gender = Gender.none if not isinstance(g, Gender) else g

	def to_mp3(self):
		# mp3 is a compressed music format
		return Song(
			name = self.name,
			starred = self.starred,
			duration = self.duration * 0.6,
			gender = self.gender
		)

	def print_animated_name(self, letters_on_screen = 5):
		buffer = f"{' '*letters_on_screen}{self.name}{' '*letters_on_screen}"

		for k in range(len(buffer)):
			print(buffer[k:k + letters_on_screen], end = '\r')
			time.sleep(0.2)

class MusicAppComponent(ABC):
	@abstractmethod
	def play_song(self, name):
		pass

class MusicApp(MusicAppComponent):
	def __init__(self, premium = False):
		self.__songs = []
		self.__is_premium = premium
		self.__dark_mode = False

	def play_song(self, name):
		songs = [s for s in self.__songs if s.name == name]

		if len(songs) == 0:
			print('Canción no encontrada...')
			return None

		# "start song" and return it
		print(f"Iniciando canción {name}.")

		return songs[0]

	def add_song(self, song):
		if not self.__is_premium and len(self.__songs) >= 5:
			return
		
		self.__songs.append(song)

	def get_starred_songs(self):
		return [m for m in self.__songs if m.starred]

	def get_sorted(self):
		return sorted(self.__songs, key = lambda x: x.duration)

	def use_dark_mode(self, use):
		self.__dark_mode = use if self.__is_premium else False

	def is_dark_mode_activated(self):
		return self.__dark_mode
