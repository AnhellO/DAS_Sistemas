from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def __init__(self, name: str):
        self._name = name

    @property
    def get_name(self) -> str:
        return self._name

    def make_sound(self):
        return 'Roar'


class Mouse(Animal):
    def __init__(self, name: str):
        self._name = name

    @property
    def get_name(self) -> str:
        return self._name

    def make_sound(self):
        return 'Squeak'
