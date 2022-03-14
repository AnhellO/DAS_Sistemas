from abc import ABC, abstractmethod
 
class Poligono(ABC):

    @abstractmethod
    def Num_lados(self):
        pass

###Sobrescribiendo el método abstracto Num_lados para los siguientes tipos de figuras:

class Triangulo(Poligono):      # Triángulo
    def Num_lados(self):
        lados = 3
        return lados

class Cuadrado(Poligono):       # Cuadrado
    def Num_lados(self):
        lados = 4
        return lados

class Pentagono(Poligono):       # Pentágono
    def Num_lados(self):
        lados = 5
        return lados

class Hexagono(Poligono):       # Hexágono
    def Num_lados(self):
        lados = 6
        return lados

if __name__ == "__main__":
    Triangulo = Triangulo()
    print(Triangulo.Num_lados())

    Cuadrado = Cuadrado()
    print(Cuadrado.Num_lados())
    
    Pentagono = Pentagono()
    print(Pentagono.Num_lados())
    
    Hexagono = Hexagono()
    print(Hexagono.Num_lados())