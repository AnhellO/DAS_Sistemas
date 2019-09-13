import abc

class Context:
    def __init__(self, movimiento):
        self._movimiento = movimiento

    def context(self):
       print('Jugamos Nivel 1 con {0}: {1}\nJugamos nivel 2 con {0}: {2} \nJugamos nivel 3 con {0}: {3} \nJugamos nivel final con {0}: {1} {2} {3}'.format(self._movimiento, self._movimiento.atacar(), self._movimiento.defender(),self._movimiento.poder_especial()))


class Videojuego(metaclass=abc.ABCMeta):
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
    print('\n')
    bowser = Bowser()
    context = Context(bowser)
    context.context()
    print('\n')
    fox = Fox()
    context = Context(fox)
    context.context()

if __name__ == '__main__':
    main()