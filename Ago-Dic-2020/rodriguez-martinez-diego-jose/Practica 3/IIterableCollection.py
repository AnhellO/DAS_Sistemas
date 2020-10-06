from abc import ABC, abstractmethod

class IIterableCollection(ABC):

    """ ''Interfaz'' para las collecciones a iterar """

    @abstractmethod
    def create_iterator(self):
        pass

