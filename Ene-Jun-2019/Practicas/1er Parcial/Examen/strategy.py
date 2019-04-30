class Videojuego(object):
	"""docstring for Videojuego"""
	
	# Solo atacar
	def nivel_1(self):
		pass

	# Solo defender
	def nivel_2(self):
		pass

	# Solo poder especial
	def nivel_3(self):
		pass

	# Atacar, luego defender, y terminar con el poder especial
	def nivel_final(self):
		pass


class Mario(object):
	"""docstring for Mario"""

	def atacar(self):
		return 'Punch!'

	def defender(self):
		return 'Roll & Protect!'

	def poder_especial(self):
		return 'Big Punch!'

	def __str__(self):
		return 'Mario'


class Bowser(object):
	"""docstring for Bowser"""

	def atacar(self):
		return 'Fire!'

	def defender(self):
		return 'Shell!'

	def poder_especial(self):
		return 'Big Fire!'

	def __str__(self):
		return 'Bowser'


class Fox(object):
	"""docstring for Fox"""

	def atacar(self):
		return 'Laser!'

	def defender(self):
		return 'Shield!'

	def poder_especial(self):
		return 'Missils!'

	def __str__(self):
		return 'Fox'