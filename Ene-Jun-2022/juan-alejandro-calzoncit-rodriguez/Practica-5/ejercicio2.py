from abc import ABC, abstractmethod
 
# Definiendo interfaz 
class LivingBeing(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(LivingBeing):
    def move(self):
        print("I can walk and run")
 
class Snake(LivingBeing):
    def move(self):
        print("I can crawl")
 
class Dog(LivingBeing):
    def move(self):
        print("I can bark")
 
class Lion(LivingBeing):
    def move(self):
        print("I can roar")


clss = [Human, Snake, Dog, Lion]

for cl in clss:
    print(f"Is {cl.__name__} subclass of LivingBeing? : {issubclass(cl,LivingBeing)}")

print()

for cl in clss:
    o = cl()
    print(f"{cl.__name__} : ")
    o.move()