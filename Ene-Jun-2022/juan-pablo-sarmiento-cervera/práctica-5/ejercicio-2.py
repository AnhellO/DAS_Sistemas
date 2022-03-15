from abc import ABC, abstractmethod

class Species(ABC):

    @abstractmethod
    def move(self):
        pass


class Human(Species):
    def move(self):
        print("I can walk and run")

class Snake(Species):
    def move(self):
        print("I can crawl")

class Dog(Species):
    def move(self):
        print("I can bark")

class Lion(Species):
    def move(self):
        print("I can roar")


if __name__ == "__main__":
    Human = Human()
    Human.move()

    Snake = Snake()
    Snake.move()

    Dog = Dog()
    Dog.move()

    Lion = Lion()
    Lion.move()