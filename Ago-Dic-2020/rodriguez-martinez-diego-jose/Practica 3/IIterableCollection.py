from abc import ABC, abstractmethod

class IIterableCollection:

    """ ''Interfaz'' para las collecciones a iterar """

    @abstractmethod
    def createIterator(self):
        pass

