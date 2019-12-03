from abc import ABCMeta, abstractmethod

class vehiculo(metaclass=ABCMeta):

    def __init__(self, tipo, modelo ):
        self._tipo = tipo
        self._modelo = modelo

    @abstractmethod
    def traslado(self):
        pass

    def get_Tipo(self):
        return self._tipo
