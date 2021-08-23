from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def equip(self):
        pass
