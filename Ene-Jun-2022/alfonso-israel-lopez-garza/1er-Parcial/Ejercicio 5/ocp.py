from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        return self.nombre

class Sonido(ABC):
    def __init__(self, obj) -> None:
        self.obj = obj

    @abstractmethod
    def Sonido(self):
        pass

class SonidoLeon(Sonido):
    def Sonido(self):
        return 'Roar'

class SonidoRaton(Sonido):
    def Sonido(self):
        return 'Squeak'

def main():
    leon = Animal('León')
    print(leon.get_nombre())
    sonido = SonidoLeon(leon)
    print(sonido.Sonido() +"\n")

    raton = Animal('Ratón')
    print(raton.get_nombre())
    sonido = SonidoRaton(raton)
    print(sonido.Sonido() +"\n")

if __name__ == "__main__":
    main()