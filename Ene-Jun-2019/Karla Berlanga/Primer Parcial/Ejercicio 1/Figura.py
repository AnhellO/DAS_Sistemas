"""
Elabore una clase Figura. De esta clase heredarán las clases Circulo, Triangulo y Rectangulo:
Para cada clase, agregar la función area
Para cada clase, sobreescribe la función __str__, para poder obtener una representación del objeto como string
Para finalizar, elabora una clase principal (main), en la cual crees y juegues con al menos 5 instancias diferentes (en total) para cada una de las clases pedidas anteriorment
"""
import math

class Figura(object):

    def __init__(self, **medidas):
        self.base = medidas if medidas.get('base') else 0
        self.altura = medidas if medidas.get('area') else 0
        self.radio = medidas if medidas.get('radio') else 0

    def area(self): pass


class Circulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.radio = arg.get('radio')

    def area(self):
        area = math.pi *(self.radio*self.radio)
        return area

    def __str__(self):
        return """
        El área del circulo de radio {} es: {}
        """.format(self.radio, "{0:.2f}".format(self.area())).strip()

class Triangulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.base = arg.get('base')
        self.altura = arg.get('altura')

    def area(self):
        area = (self.base*self.altura)/2
        return area

    def __str__(self):
        return """
        El area del triángulo de base {}  y altura {} es: {}
        """.format(self.base, self.altura, "{0:.2f}".format(self.area())).strip()

class Rectangulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.base = arg.get('base')
        self.altura = arg.get('altura')

    def area(self):
        area = (self.base*self.altura)
        return area

    def __str__(self):
        return """
        El area del rectángulo de base {}  y altura {} es: {}
        """.format(self.base, self.altura, "{0:.2f}".format(self.base*self.altura)).strip()


def main():
    circulo = Circulo(radio = 8)
    print(circulo)

    triangulo = Triangulo(base = 5, altura = 10)
    print(triangulo)

    rectangulo = Rectangulo(base = 10, altura = 4)
    print(rectangulo)


if __name__ == '__main__':
    main()
