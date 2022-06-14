from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Entity):
    def move(self):
        print("I can walk and run")


class Snake(Entity):
    def move(self):
        print("I can crawl")


class Dog(Entity):
    def move(self):
        print("I can bark")


class Lion(Entity):
    def move(self):
        print("I can roar")


if __name__ == '__main__':
    Human().move()
    Snake().move()
    Dog().move()
    Lion().move()