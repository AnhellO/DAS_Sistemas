import math
class Figura:
    def __init__(self, radio, base, altura):
        self.radio = radio.title()
        self.base = base.title()
        self.altura = altura.title()

#MÉTODOS GET
    def get_radio(self):
        return self.radio
    def get_base(self):
        return self.base
    def get_altura(self):
        return self.altura

#CLASE CÍRCULO
class Circulo(Figura):
    print("Area del circulo")
    ##FUNCION AREA
    def area(radio):
        area = math.pi*(radio*radio)
        return area
    #FUNCION __STR__
    def __str__(self):
        return """
                El área del circulo de radio {} es: {}
                """.format(self.radio, "{0:.2f}".format(self.area())).strip()
    #MAIN
    if __name__ == '__main__':
       print(area(5))
       print(area(4))
       print(area(3))
       print(area(2))
       print(area(1))

#CLASE TRIANGULO
class Triangulo(Figura):
    print("Area del triangulo")
    #FUNCION AREA
    def area(base,altura):
        area = (base*altura)/2
        return area
    #FUNCION __STR__
    def __str__(self):
        return """
                El área del triangulo de base {} y altura {} es: {}
                """.format(self.base, self.altura, "{0:.2f}".format(self.area())).strip()
    #MAIN
    if __name__ == '__main__':
        print(area(2,6))
        print(area(5,5))
        print(area(8,10))
        print(area(5,3))
        print(area(11,9))

#CLASE RECTANGULO
class Rectangulo(Figura):
    print("Area del rectangulo")
    #FUNCION AREA
    def area(base,altura):
        area = base*altura
        return area
    #FUNCION __STR__
    def __str__(self):
        return """
                El área del rectangulo de base {} y altura {} es: {}
                """.format(self.base, self.altura, "{0:.2f}".format(self.area())).strip()
    #MAIN
    if __name__ == '__main__':
        print(area(2,6))
        print(area(5,5))
        print(area(8,10))
        print(area(5,3))
        print(area(11,9))