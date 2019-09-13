"""
Proporcionar un sustituto o marcador de posicion para otro
objeto para  controlar el acceso a este o agregar otras
responsabilidades.
"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define la interfaz comun para RealSubject y proxypara que
    Proxy se pueda usar en cualquier lugar donde se espera un
    RealSubject.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Mantiene una referencia que le permite al Proxy acceder
    al RealSubject, proporciona una interfaz identica a la original.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ...
        self._real_subject.request()
        # ...


class RealSubject(Subject):
    """
    Define el objeto real que representa el Proxy.
    """

    def request(self):
        pass


def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()


if __name__ == "__main__":
    main()
