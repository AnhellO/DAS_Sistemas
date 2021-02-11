from abc import ABC, abstractmethod

class IIterator(ABC):

    """ ''Interfaz'' para los Iteradores """

    @abstractmethod
    def get_next(self, iterable):
        """ Regresa el siguiente elemento del iterable """
        pass

    @abstractmethod
    def has_more(self):
        """ Regresa True si hay mas elementos en el iterable, False si no """
        pass
    