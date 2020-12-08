import math

class Figura(object):
    """Clase Figura"""
    def area(self):
        pass

class Circulo(Figura):
    """Clase Circulo que hereda de la clase Figura"""
    def __init__(self, radio):  # Constructor
        self.radio = radio

    def area(self):  # Calcular el área de un círculo
        return math.pi * (self.radio ** 2)

    def __str__(self):  # Mostrar área del círculo
        return "Área círculo: {}".format(self.area())


class Triangulo(Figura):
    """Clase Triangulo que hereda de la clase Figura"""
    def __init__(self, base, altura):  # constructor
        self.base = base
        self.altura = altura

    def area(self):  # calcular el área de un triángulo
        return (self.base * self.altura) / 2

    def __str__(self):  # Mostrar área del triángulo
        return "Área triángulo: {}".format(self.area())


class Rectangulo(Figura):
    """Clase Rectangulo que hereda de la clase Figura"""
    def __init__(self, base, altura):  # Constructor
        self.base = base
        self.altura = altura

    def area(self):  # calcular el área de un rectángulo
        return self.base * self.altura

    def __str__(self):  # Mostrar el área de un rectángulo
        return "Área rectángulo: {}".format(self.area())

def main():
    # Instanciar cinco objetos diferentes
    circulo = Circulo(3)  # creamos círculos
    print(circulo)
    circulo2 = Circulo(1)
    print(circulo2)
    triangulo = Triangulo(3, 4)  # creamos un triángulo
    print(triangulo)
    rectangulo = Rectangulo(3, 5)  # creamos dos rectángulos
    print(rectangulo)
    rectangulo2 = Rectangulo(2, 11)
    print(rectangulo2)

if __name__ == '__main__':
    main()