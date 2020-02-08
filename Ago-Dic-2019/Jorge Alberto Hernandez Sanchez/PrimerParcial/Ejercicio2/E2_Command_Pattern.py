from abc import ABCMeta, abstractmethod
#Clase Abstracta
class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class encender(Command):
    def __init__(self, encender):
        self._encender = encender

    def execute(self):
        print(self._encender)

class ComandoApagar(Command):
    def __init__(self, apagar):
        self._apagar = apagar

    def execute(self):
        print(self._apagar)

class CmdCambiarCanal(Command):
    def __init__(self, cambiarCanal, canal):
        self._cambiarCanal = cambiarCanal
        self._canal = canal

    def execute(self):
        print(self._cambiarCanal, 'canal cambio al '+ self._canal)

class VolumenUP(Command):
    def __init__(self, subirVolumen):
        self._subirVolumen = subirVolumen

    def execute(self):
        print(self._subirVolumen)

class VolumenDown(Command):
    def __init__(self, VolumenD):
        self._VolumenD = VolumenD

    def execute(self):
        print(self._VolumenD)

"""Invocador"""
class ControlRemoto():

    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

class Television():
    """docstring for Television"""

    def encender(self):
        print('Encendida!')

    def apagar(self):
        print('Apagada!')
# no se poruq me marca error en esta funcion
#intente poniendo a todas self pero me pedian sel como parametro
    def cambiarCanal(numCanal):
        print('Se cambio al canal + numCanal')

    def subirVolumen(self):
        print('Subimos volumen!')

    def bajarVolumen(self):
        print('Bajamos volumen!')

def main():
    tv = Television()
    Encender = encender(tv)

    control = ControlRemoto(Encender)
    control.invoke()

if __name__ == '__main__':
    main()