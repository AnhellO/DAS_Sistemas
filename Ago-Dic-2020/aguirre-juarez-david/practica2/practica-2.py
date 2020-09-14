
class Entity:
	def __init__(self, name, x = 0.0, y = 0.0):
		self.__name = name.capitalize()
		self.__x = x
		self.__y = y
		self.__death = False
		self.__killedBy = None

	def __str__(self):
		return f"{self.getName()} {('with live' if not self.isDeath() else self.deathMessage())}, position: <{self.__x},{self.__y}>"

	def deathMessage(self):
		if self.__death:
			if isinstance(self.__killedBy, Entity):
				return f'killed by {self.__killedBy.getName()}'
			return 'killed'
		return ''

	def setPos(self, x, y):
		self.__x = x
		self.__y = y

	def move(self, x, y):
		self.__x += x
		self.__y += y

	def isDeath(self):
		return self.__death

	def kill(self, by):
		self.__death = True
		self.__killedBy = by

	def getName(self):
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

	def isDeath(self):
		if self.__health <= 0.0:
			self.kill()

		return super().isDeath()


	def hurt(self, by):
		if(isinstance(by, Player)):
			self.__health -= (1 - self.__protection) * abs(by.__strength)
			self.isDeath()

	def setHealth(self, health):
		self.__health = health
		self.isDeath()

	def getHealth(self):
		return self.__health

	def setProtection(self, protection):
		self.__protection = abs(protection) % 1

	def getProtection(self):
		return self.__protection

	def setStrength(self, strength):
		self.__strength = abs(strength)

	def getStrength(self):
		return self.__strength