from abc import ABCMeta, abstractmethod

class Comando(metaclass=ABCMeta):
    @abstractmethod
    def ejecutar(self):
        pass

# Receiver
class Television():
    """docstring for Television"""

    def encender(self):
        print('Encendida!')

    def apagar(self):
        print('Apagada!')

    def cambiarCanal(numCanal):
        print('Cambiamos al canal'.format(numCanal))

    def subirVolumen(self):
        print('Subimos volumen!')

    def bajarVolumen(self):
        print('Bajamos volumen!')

class encender(Comando):
    def __init__(self, encender):
        self._encender = encender

    def ejecutar(self):
        print(self._encender)

class ComandoApagar(Comando):
    def __init__(self, apagar):
        self._apagar= apagar

    def ejecutar(self):
        print(self._apagar)

class ComandoCambiarCanal(Comando):
    def __init__(self, cambiarCanal, canal):
        self._cambiarCanal = cambiarCanal
        self._canal = canal

    def ejecutar(self):
        print(self._cambiarCanal, self._canal)

class SubirVolumen(Comando):
    def __init__(self, subirVolumen):
        self._subirVolumen = subirVolumen

    def ejecutar(self):
        print(f"{self._subirVolumen}")

class BajarVolumen(Comando):
    def __init__(self, bajarVolumen):
        self._bajarVolumen = bajarVolumen

    def ejecutar(self):
        print(self._bajarVolumen)

#Invoker
class ControlRemoto():
    """docstring for ControlRemoto"""
    def __init__(self, comando):
        self.comando= comando

    def set_comando(self, comando):
        self.comando = comando

    def invoke(self):
        self.comando.ejecutar()


def main():
    tv = Television()
    tv.encender()
    Encender = encender(tv)
    control = ControlRemoto(Encender)
    control.invoke()

if __name__ == '__main__':
    main()