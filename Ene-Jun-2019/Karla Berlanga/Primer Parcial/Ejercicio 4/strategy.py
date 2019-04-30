"""
Para el ejemplo de código en el archivo strategy.py:
Implementa la funcionalidad necesaria utilizando el patrón de diseño Strategy para que se puedan jugar los 4 niveles del videojuego con los tres diferentes personajes en una sola ejecución del programa
Ejemplo para un personaje:
Jugamos nivel 1 con Bowser: Fire!
Jugamos nivel 2 con Bowser: Shell!
Jugamos nivel 3 con Bowser: Big Fire!
Jugamos nivel final con Bowser: Fire! Shell! Big Fire!
Explica la lógica implementada detrás de tu enfoque
"""
import abc

#Context: Aqui se define la interfaz para los clientes
class Context:

    def __init__(self, videojuego):
        self._videojuego = videojuego

    def context(self):
        print(
        "Jugamos nivel 1 con {0} : {1}\nJugamos nivel 2 con {0}: {2} \nJugamos nivel 3 con {0}: {3} \nJugamos nivel final con {0}: {1} {2} {3}"
        .format(self._videojuego, self._videojuego.atacar(), self._videojuego.defender(),self._videojuego.poder_especial())
        )


#Strategy: Esta es la interfaz comun para todos los ConcreteStrategy,
#es decir, el comportamiento es comun entre estos
class Videojuego(metaclass=abc.ABCMeta):
	"""docstring for Videojuego"""

	# Solo atacar
	def atacar(self):
		pass

	# Solo defender
	def defender(self):
		pass

	# Solo poder especial
	def poder_especial(self):
		pass

	# Atacar, luego defender, y terminar con el poder especial
	def nivel_final(self):
		pass

#ConcreteStrategy: aquí se implementa el algoritmo usando
#la interfaz Strategy(Videojuego) y como podemos ver
#comparten el comportamiento
class Mario(Videojuego):
	"""docstring for Mario"""

	def atacar(self):
		return 'Punch!'

	def defender(self):
		return 'Roll & Protect!'

	def poder_especial(self):
		return 'Big Punch!'

	def __str__(self):
		return 'Mario'

#ConcreteStrategy
class Bowser(Videojuego):
	"""docstring for Bowser"""

	def atacar(self):
		return 'Fire!'

	def defender(self):
		return 'Shell!'

	def poder_especial(self):
		return 'Big Fire!'

	def __str__(self):
		return 'Bowser'

#ConcreteStrategy
class Fox(Videojuego):
	"""docstring for Fox"""

	def atacar(self):
		return 'Laser!'

	def defender(self):
		return 'Shield!'

	def poder_especial(self):
		return 'Missils!'

	def __str__(self):
		return 'Fox'

def main():
    mario = Mario()
    context = Context(mario)
    context.context()

    print("\n")
    bowser = Bowser()
    context = Context(bowser)
    context.context()

    print("\n")
    fox  = Fox()
    context = Context(fox)
    context.context()




if __name__ == "__main__":
    main()
