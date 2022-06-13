from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nombre = None) -> None:
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        return self.nombre

class sonido_animal(ABC):
    def __init__(self, obj):
        self.obj = obj
    
    @abstractmethod
    def sonido(self) -> str:
        pass

class Sonido_leon(sonido_animal):
    def sonido(self) -> str:
        return "roar"

class Sonido_raton(sonido_animal):
    def sonido(self) -> str:
        return "squeak"

def main():
    a = Animal()
    a.nombre = "leon"
    print(a.get_nombre())
    
    sonido = Sonido_leon(a)
    print(sonido.sonido())

    b = Animal()
    b.nombre = "raton"
    print(b.get_nombre())
    
    sonido = Sonido_raton(b)
    print(sonido.sonido())

if __name__ == "__main__":
    main()
# class Animal:
#     def _init_(self, nombre: str):
#         self.nombre = nombre

#     def get_nombre(self) -> str:
#         pass

# animales = [
#     Animal('león'),
#     Animal('ratón')
# ]

# def sonido_animal(animales: list):
#     for animal in animales:
#         if animal.nombre == 'león':
#             print('roar')

#         elif animal.nombre == 'ratón':
#             print('squeak')

# sonido_animal(animales)