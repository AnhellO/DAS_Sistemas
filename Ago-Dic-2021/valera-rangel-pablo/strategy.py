import abc
from random import randint

# Interfaz Estrategia


class ChoosePlayStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

# Estrategia Concreta: Tierra


class rushPlayStrategy(ChoosePlayStrategy):
    def play(self):
        return 'Jugando por tierra'

# Estrategia Concreta: Aire


class passPlayStrategy(ChoosePlayStrategy):
    def play(self):
        return 'Jugando por aire'

# Estrategia Concreta: Despeje


class puntPlayStrategy(ChoosePlayStrategy):
    def play(self):
        return 'Intento de Despeje'

# Estrategia Concreta: Gol de Campo


class fieldGoalPlayStrategy(ChoosePlayStrategy):
    def play(self):
        return 'Intento de gol de campo'


# Contexto
class playContext(object):
    def __init__(self, yardas, oportunidad, YardaCampo, strategy: ChoosePlayStrategy = None):
        self._yardas = yardas
        self._oportunidad = oportunidad
        self._YardaCampo = YardaCampo
        self._strategy = strategy

    def play_context(self):

        if self._strategy != None:
            return self._strategy.play()

        if self._oportunidad <= 3 and self._yardas <= 5:
            return rushPlayStrategy.play(self)

        if self._oportunidad == 4 and self._yardas >= 5 and self._YardaCampo < 70:
            return puntPlayStrategy.play(self)

        if self._oportunidad == 4 and self._yardas >= 1 and self._YardaCampo >= 70:
            return fieldGoalPlayStrategy.play(self)

        return passPlayStrategy.play(self)

    def set_strategy(self, strategy: ChoosePlayStrategy):
        self._strategy = strategy


def main():
    yardas = 15  # randint(1, 15)
    oportunidad = 4  # randint(1, 4)
    yardasCampo = 78  # randint(1, 99)

    print(
        f'Oportunidad: {oportunidad}\n Yardas: {yardas}\n Balon en la yarda: {yardasCampo}')
    context = playContext(yardas, oportunidad, yardasCampo)

    print(context.play_context())


#Forzamos a jugar por tierra
    rushPlay = rushPlayStrategy()
    context.set_strategy(rushPlay)
    print(context.play_context())

#Forzamos a jugar por aire
    passPlay = passPlayStrategy()
    context.set_strategy(passPlay)
    print(context.play_context())


if __name__ == '__main__':
    main()
