from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def __init__(self,nombre_del_animal):
        self.nombre_del_animal=nombre_del_animal
        self.como_me_muevo=""
    
    @abstractmethod
    def move(self):
        print (self.como_me_muevo)

class Human(animal):
    def __init__(self, nombre_del_animal):
        super().__init__(nombre_del_animal)
        self.como_me_muevo="I can walk and run"
    def move(self):
        return super().move()

class Snake(animal):
    def __init__(self, nombre_del_animal):
        super().__init__(nombre_del_animal)
        self.como_me_muevo="I can crawl"
    def move(self):
        return super().move()

class Dog(animal):
    def __init__(self, nombre_del_animal):
        super().__init__(nombre_del_animal)
        self.como_me_muevo="I can bark"
    def move(self):
        return super().move()

class Lion(animal):
    def __init__(self, nombre_del_animal):
        super().__init__(nombre_del_animal)
        self.como_me_muevo="I can roar"
    def move(self):
        return super().move()



    