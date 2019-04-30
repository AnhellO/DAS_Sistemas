import math

class Figura():
    def __init__(self, **args):
        self.tipo = args.get('tipo')

class Circulo(Figura):
    def area(radio):
        if radio < 0:
            return "No Valido"
        return math.pi * (radio * radio)

    def __str__(self):
        return """
        Tipo: {}\nArea: {}
        """.format(self.tipo, self.area()).strip()

class Triangulo(Figura):
    def area(h, b):
        return 0.50*h*b

    def __str__(self):
        return """
        Tipo: {}\nArea: {}
        """.format(self.tipo, self.area()).strip()

class Rectangulo(Figura):
    def area(h,b):
        return h*b
    def __str__(self):
        return """
        Tipo: {}\nArea: {}
        """.format(self.tipo, self.area()).strip()

if __name__ == '__main__':
    figura_1 = Figura(tipo= 'Circulo')
    circulo = Circulo.area(8)
    print("El Area del Circulo es: ",circulo)

    figura_2 = Figura(tipo='Triangulo')
    triangulo = Triangulo.area(8,7)
    print("El Area del Triangulo es: ",triangulo)

    figura_3 = Figura(tipo='Rectangulo')
    rectangulo = Rectangulo.area(10,6)
    print("El Area del Rectangulo es: ",rectangulo)

    figura_4 = Figura(tipo='Rectangulo')
    rectangulo1 = Rectangulo.area(18, 15)
    print("El Area del Rectangulo es: ", rectangulo1)

    figura_5 = Figura(tipo='Triangulo')
    triangulo1 = Rectangulo.area(6, 8)
    print("El Area del Triangulo es: ", triangulo1)