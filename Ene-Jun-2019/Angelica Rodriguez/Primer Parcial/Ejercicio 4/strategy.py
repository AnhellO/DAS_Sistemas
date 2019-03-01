import abc

# Para el ejemplo de código en el archivo strategy.py:
# Implementa la funcionalidad necesaria utilizando el patrón de diseño
# Strategy para que se puedan jugar los 4 niveles del videojuego con los
# tres diferentes personajes en una sola ejecución del programa
# Ejemplo para un personaje:
# Jugamos nivel 1 con Bowser: Fire!
# Jugamos nivel 2 con Bowser: Shell!
# Jugamos nivel 3 con Bowser: Big Fire!
# Jugamos nivel final con Bowser: Fire! Shell! Big Fire!
# Explica la lógica implementada detrás de tu enfoque

class Context:
	def __init__(self, strategy): # constructor
		self._strategy = strategy

    # solo atacar
	def nivel_1(self):
		return self._strategy.atacar()

	# Solo defender
	def nivel_2(self):
		return self._strategy.defender()

	# Solo poder especial
	def nivel_3(self):
		return self._strategy.poder_especial()

	# Atacar, luego defender, y terminar con el poder especial
	def nivel_final(self):
		return self._strategy.atacar()+" " +self._strategy.defender()+" "+self._strategy.poder_especial()

    # imprimimos el nombre del juego junto con las estrategias correspondientes a cada nivel
	def context(self):
		print("Jugamos el nivel 1 con {}: {}".format(self._strategy, self.nivel_1()))
		print("Jugamos el nivel 2 con {}: {}".format(self._strategy, self.nivel_2()))
		print("Jugamos el nivel 3 con {}: {}".format(self._strategy, self.nivel_3()))
		print("Jugamos el nivel final con {}: {}\n".format(self._strategy, self.nivel_final()))

# Clase que contiene todos los métodos de las clases Mario, Bowser y Fox
class Strategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def atacar(self):
		pass

	@abc.abstractmethod
	def defender(self):
		pass

	@abc.abstractmethod
	def poder_especial(self):
		pass

class Mario(Strategy):
	"""docstring for Mario"""

	def atacar(self):
		return 'Punch!'

	def defender(self):
		return 'Roll & Protect!'

	def poder_especial(self):
		return 'Big Punch!'

	def __str__(self):
		return 'Mario'

class Bowser(Strategy):
	"""docstring for Bowser"""

	def atacar(self):
		return 'Fire!'

	def defender(self):
		return 'Shell!'

	def poder_especial(self):
		return 'Big Fire!'

	def __str__(self):
		return 'Bowser'

class Fox(Strategy):
	"""docstring for Fox"""

	def atacar(self):
		return 'Laser!'

	def defender(self):
		return 'Shield!'

	def poder_especial(self):
		return 'Missils!'

	def __str__(self):
		return 'Fox'

# Explicación: strategy es un patrón de comportamiento porque el usuario
# puede elegir el objeto que necesita e intercambiarlo dinámicamente
# según sus necesidades. En este caso podemos elegir entre mario, boswer y fox.

def main():
	mario = Mario()
	context = Context(mario)
	context.context()

    # Juego Bowser
	bowser = Bowser()
	context = Context(bowser)
	context.context()

    # Juego Fox
	fox = Fox()
	context = Context(fox)
	context.context()

if __name__ == '__main__':
	main()
