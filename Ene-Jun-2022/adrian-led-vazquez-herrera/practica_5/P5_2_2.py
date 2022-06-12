#DAS Práctica 5.2.2

from abc import ABC, abstractmethod

class animal(ABC):
    
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    
    def move(self):
        print("I can walk and run")
 
class Snake(animal):
    
    def move(self):
        print("I can crawl")
 
class Dog(animal):
    
    def move(self):
        print("I can bark")
 
class Lion(animal):
    
    def move(self):
        print("I can roar")
        
        
Juan=Human()
Jormungandrr=Snake()
Krypto=Dog()
Simba=Lion()
creatures=[Juan, Jormungandrr, Krypto, Simba]

for animal in creatures:
    animal.move()