"""
Convierte la interfaz de una clase en otra interfaz que los clientes esperan.
El adaptador permite que las clases trabajen juntas de otra manera que no serían posibles debido a interfaces incompatibles
"""

import abc


class Target(metaclass=abc.ABCMeta):
    """
    Defina la interfaz específica de dominio que utiliza el Cliente.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapte la interfaz de Adaptee a la interfaz de destino.
    """

    def request(self):
        self._adaptee.specific_request()


class Adaptee:
    """
    Defina una interfaz existente que necesite adaptación.
    """

    def specific_request(self):
        pass


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()