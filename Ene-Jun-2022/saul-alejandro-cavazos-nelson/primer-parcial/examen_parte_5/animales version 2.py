from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def __init__(self, nombre: str):
        self.nombre = nombre
    @abstractmethod
    def get_nombre(self) -> str:
        return self.nombre
    @abstractmethod
    def sonido_animal(self)->str:
        pass

class leon(Animal):
    def __init__(self):
        super().__init__("leon")
    def get_nombre(self) -> str:
        return super().get_nombre()
    def sonido_animal(self) -> str:
        return "roar"

class raton(Animal):
    def __init__(self):
        super().__init__("raton")
    def get_nombre(self) -> str:
        return super().get_nombre()
    def sonido_animal(self) -> str:
        return "squeak"


#se crearia una nueva clase para agregar un nuevo animal 
if __name__ == "__main__":
    print(raton().get_nombre())
    print(raton().sonido_animal())
