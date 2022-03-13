from abc import ABC, abstractmethod
 
class LivingBeings(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(LivingBeings):
    '''
    En la funcion move aqui regresamos un string, de esta manera
    no se imprimira el None implícito por que la función
    termina sin retornar nada.
    '''
    def move(self) -> str:
        movimiento = "I can walk and run"
        return movimiento
 
class Snake(LivingBeings):
    def move(self):
        print("I can crawl")
 
class Dog(LivingBeings):
    def move(self):
        print("I can bark")
 
class Lion(LivingBeings):
    def move(self):
        print("I can roar")

if __name__ == "__main__":
    humano = Human()
    serpiente = Snake()
    perro = Dog()
    leon = Lion()

    print(humano.move())
    print(serpiente.move())

