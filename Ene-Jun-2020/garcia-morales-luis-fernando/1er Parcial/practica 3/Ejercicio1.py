from abc import abstractmethod
import copy
class Oveja(object):
    @abstractmethod
    def clonar():
        pass
        
class Dolly(Oveja):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo
    def __str__(self):
        return f"Nombre: {self.nombre}\nTipo:{self.tipo}"    
    def clonar(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    protodolly = Dolly("Dolly", "domestica")
    print(protodolly)
    protodally = protodolly.clonar()
    protodally.set_nombre("dally")
    protodally.set_tipo("Libre laik di eir")
    print(protodally)
