from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class CalculadorArea:
    def __init__(self, figuras):
        assert isinstance(figuras, list)
        self.figuras = figuras

    def suma_areas(self):
        total = 0
        for figura in self.figuras:
            total += figura.calcular_area()
        return total

def main():
    r = Rectangulo(3, 4)
    r1 = Rectangulo(10, 15)
    r2 = Rectangulo(5, 7)
    calc = CalculadorArea([r, r1, r2])
    print(calc.suma_areas())

if __name__ == '__main__':
    main()

#¿Que sucederia si quisieramos sumar las areas de otros tipos de figuras?
#Tendriamos que crear una clase para dicha figura, que herede de la clase Figura

#¿Que tendriamos que hacer para poder sumar volumenes ademas de areas?
#Tendriamos que crear una clase que contenga un calculador de volumen, despues de eso creariamos
#las funciones como en calcular_area
