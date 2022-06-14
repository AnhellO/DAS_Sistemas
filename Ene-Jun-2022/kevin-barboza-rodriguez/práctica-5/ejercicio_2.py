from abc  import ABC, abstractmethod

class Ser(ABC):
    @abstractmethod
    def action(self):
        print("what can you do?")

class Human(Ser):

    def action(self):
        super().action()
        print("I can walk and run\n")
 
class Snake(Ser):
    def action(self):
        super().action()
        print("I can crawl\n")
 
class Dog(Ser):
    def action(self):
        super().action()
        print("I can bark\n")
 
class Lion(Ser):
    def action(self):
        super().action()
        print("I can roar\n")


if __name__ == "__main__":

    human = Human()
    human.action()

    snake = Snake()
    snake.action()

    dog = Dog()
    dog.action()

    lion = Lion()
    lion.action()