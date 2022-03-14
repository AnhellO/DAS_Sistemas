from abc import ABC, abstractmethod

class whatCanYouDo(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(whatCanYouDo):
    def move(self):
        print("I can walk and run")

class Snake(whatCanYouDo):
    def move(self):
        print("I can crawl")

class Dog(whatCanYouDo):
    def move(self):
        print("I can bark")

class Lion(whatCanYouDo):
    def move(self):
        print("I can roar")

if __name__ == "__main__":
    hum = Human()
    snk = Snake()
    dg  = Dog()
    lon = Lion()

    hum.move()
    snk.move()
    dg.move()
    lon.move()