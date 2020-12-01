
class Entity:
	def __init__(self, name, x = 0.0, y = 0.0):
		self.__name = name.capitalize()
		self.__x = x
		self.__y = y
		self.__death = False
		self.__killed_by = None

	def __str__(self):
		return f"{self.get_name()} {('with live' if not self.is_death() else self.death_message())}, position: <{self.__x},{self.__y}>"

	def death_message(self):
		if not self.__death:
			return ''

		if isinstance(self.__killed_by, Entity):
			return f'killed by {self.__killed_by.get_name()}'

		return 'killed'

	def set_pos(self, x, y):
		self.__x = x
		self.__y = y

	def move(self, x, y):
		self.__x += x
		self.__y += y

	def is_death(self):
		return self.__death

	def kill(self, by):
		self.__death = True
		self.__killed_by = by

	def get_name(self):
		return self.__name

class Player(Entity):
	def __init__(self, name, x = 0.0, y = 0.0):
		super().__init__(name, x, y)
		self.__health = 10.0
		self.__strength = 3.0
		self.__protection = 0.2

	def kill(self, by):
		super().kill(by)
		self.__health = 0.0

	def is_death(self):
		if self.__health <= 0.0:
			self.kill()

		return super().is_death()


	def hurt(self, by):
		if(isinstance(by, Player)):
			self.__health -= (1 - self.__protection) * abs(by.__strength)
			self.is_death()

	def set_health(self, health):
		self.__health = health
		self.is_death()

	def get_health(self):
		return self.__health

	def set_protection(self, protection):
		self.__protection = abs(protection) % 1

	def get_protection(self):
		return self.__protection

	def set_strength(self, strength):
		self.__strength = abs(strength)

	def get_strength(self):
		return self.__strength