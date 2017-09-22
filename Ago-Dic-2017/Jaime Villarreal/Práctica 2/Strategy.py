import abc

# Strategy Design Pattern en un RPG.

# Objetivo: Crear clases de personajes con métodos individuales para lograr un objetivo común.

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    # Se definen las funciones generales de cada personaje sin importar su clase.
    def context_interface(self):
        self._strategy.attack()
        self._strategy.defend()
        self._strategy.level_up()


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def defend(self):
        pass

    @abc.abstractmethod
    def level_up(self):
        pass


class Knight(Strategy):
    # Caballero: Resistente a daño, no ataca a distancia ni con magia.

    def attack(self):
        print("¡Ataco usando armas de cuerpo a cuerpo!")

    def defend(self):
        print("Puedo utilizar armaduras pesadas sin problema.")

    def level_up(self):
        print("Level up: +15 HP / +5 Mana / +30 Capacidad")


class Paladin(Strategy):
    # Paladin: Punto medio entre magos y caballeros, no combate cuerpo a cuerpo.

    def attack(self):
        print("¡Ataco usando armas a distancia!")

    def defend(self):
        print("Puedo utilizar armaduras medianas y algunas capas.")

    def level_up(self):
        print("Level up: +10 HP / +10 Mana / +20 Capacidad")


class Sorcerer(Strategy):
    # Hechizero: Maestro de los elementos fuego y energía, frágil en combate.

    def attack(self):
        print("¡Ataco usando los elementos de fuego y energía!")

    def defend(self):
        print("Prefiero usar capas todo el tiempo.")

    def level_up(self):
        print("Level up: +5 HP / +30 Mana / +10 Capacidad")


class Druid(Strategy):
    # Druida: Domina los elementos hielo y tierra con capacidades curativas, frágil en combate.

    def attack(self):
        print("¡Ataco usando los elementos de hielo y tierra!")

    def defend(self):
        print("Prefiero usar capas todo el tiempo y curar a los que me rodean.")

    def level_up(self):
        print("Level up: +5 HP / +30 Mana / +10 Capacidad")


def main():
    knight = Knight()
    paladin = Paladin()
    sorcerer = Sorcerer()
    druid = Druid()

    context = Context(knight)
    context.context_interface()

    context = Context(paladin)
    context.context_interface()

if __name__ == "__main__":
    main()
