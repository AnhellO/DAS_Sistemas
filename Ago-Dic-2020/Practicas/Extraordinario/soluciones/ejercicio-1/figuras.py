import math, abc

class Figura(metaclass=abc.ABCMeta):
    """Class Figura"""
    @abc.abstractmethod
    def area(self):
        pass

class Circulo(Figura):
    """Class Circulo"""
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return "Área Círculo: {}".format(self.area())


class Triangulo(Figura):
    """Class Triangulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        return "Área Triángulo: {}".format(self.area())


class Rectangulo(Figura):
    """Class Rectangulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def __str__(self):
        return "Área Rectángulo: {}".format(self.area())


def filtrar(figuras: list, tipo: str) -> list:
    """
    filtrar devuelve una nueva lista de figuras después de filtrar por el tipo de figura especificada
    """
    new = []
    for figura in figuras:
        if figura.__class__.__name__ == tipo:
            new.append(figura)
    
    return new


def main():
    for circulo in [Circulo(1), Circulo(2), Circulo(3)]:
        print(circulo)

    for triangulo in [Triangulo(1, 5), Triangulo(2, 5), Triangulo(3, 5)]:
        print(triangulo)

    for rectangulo in [Rectangulo(1, 6), Rectangulo(2, 6), Rectangulo(3, 6)]:
        print(rectangulo)

    print("Filtrando figuras...")
    figuras = [Circulo(1), Circulo(2), Circulo(3), Triangulo(1, 5), Triangulo(2, 5), Triangulo(3, 5), Rectangulo(1, 6), Rectangulo(2, 6), Rectangulo(3, 6)]
    for figura in filtrar(figuras, "Rectangulo"):
        print(figura)

if __name__ == '__main__':
    main()