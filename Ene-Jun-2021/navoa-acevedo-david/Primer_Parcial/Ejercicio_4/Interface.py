from abc import abstractmethod, ABCMeta

#Interface del cajero
class IDcajero(metaclass=ABCMeta):
    #Metodos que se implementan
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        #Coloca el siguiente handler en la cadena

    @staticmethod
    @abstractmethod
    def handle(amount):
        #maneja el evento