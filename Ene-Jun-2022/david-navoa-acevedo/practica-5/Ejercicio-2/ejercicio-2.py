from abc import ABC,abstractmethod

#i can create basic movement as everyone have some certain of move, and from there i can create a human, snake, dog, lion
class basic_move(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(basic_move):
    def move(self):
        print("I can walk and run")
 
class Snake(basic_move):
    def move(self):
        print("I can crawl")
 
class Dog(basic_move):
    def move(self):
        print("I can bark")
 
class Lion(basic_move):
    def move(self):
        print("I can roar")