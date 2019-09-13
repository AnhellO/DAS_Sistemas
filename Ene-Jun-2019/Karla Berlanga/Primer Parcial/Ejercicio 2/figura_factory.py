"""
Implementa el patrón de diseño Factory Method tomando como referencia el ejercicio anterior, de tal manera que podamos crear múltiples instancias/figuras dentro de la misma clase main, pero ahora utilizando la factoría.
Re-utiliza todo tu código existente, pero dentro de un nuevo archivo
Crea al menos 5 nuevas instancias de diferente tipo, pero por medio del Factory
"""
from abc import ABC, abstractmethod
import math

class Figura(object):

    def __init__(self, **arg):
        self.base = arg if arg.get('base') else 0
        self.altura = arg if arg.get('altura') else 0
        self.radio = arg if arg.get('radio') else 0

    @abstractmethod
    def area(self):
        pass



class Circulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.radio = arg.get('radio')

    def area(self):
        return """
        El área del circulo de radio {} es: {}
        """.format(self.radio, "{0:.2f}".format(math.pi *(self.radio*self.radio))).strip()

class Triangulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.base = arg.get('base')
        self.altura = arg.get('altura')

    def area(self):
        return """
        El area del triángulo de base {}  y altura {} es: {}
        """.format(self.base, self.altura, "{0:.2f}".format((self.base*self.altura)/2)).strip()

class Rectangulo(Figura):
    def __init__(self, **arg):
        Figura.__init__(self, **arg)
        self.base = arg.get('base')
        self.altura = arg.get('altura')

    def area(self):
        return """
        El area del rectángulo de base {}  y altura {} es: {}
        """.format(self.base, self.altura, "{0:.2f}".format(self.base*self.altura)).strip()

class FiguraFactory(object):

    @staticmethod
    def area(**arg):
        if arg.get('tipo') == 'circulo':
            return Circulo(**arg)
        elif arg.get('tipo') == 'triangulo':
            return Triangulo(**arg)
        elif arg.get('tipo') == 'rectangulo':
            return Rectangulo(**arg)

def main():
    figura = FiguraFactory.area(tipo = 'circulo', radio = 3)
    print(figura.area())

    figura2 = FiguraFactory.area(tipo = 'triangulo', base = 4, altura = 3)
    print(figura2.area())

    figura3 = FiguraFactory.area(tipo = 'rectangulo', base = 4, altura = 3)
    print(figura3.area())

    figura4 = FiguraFactory.area(tipo = 'circulo', radio = 5)
    print(figura4.area())

    triangulo = FiguraFactory.area(tipo = 'triangulo', base = 7, altura = 5)
    print(triangulo.area())

if __name__ == "__main__":
    main()
