import math
from abc import ABC, abstractmethod

class Figura(object):

    def __init__(self, **argumentos):
        self.tipo = argumentos.get('tipo')

    @abstractmethod
    def imprime_argumentos(self):
        pass


class Circulo(Figura):
    def __init__(self, **argumentos):
        argumentos['tipo'] = 'Circulo'
        Figura.__init__(self,**argumentos)
        self.radio = argumentos.get('Radio')
    def imprime_argumentos(self):
        return 'Tipo: {}\nArea: {}'.format(self.tipo,(math.pi * (self.radio * self.radio))).strip()

class Triangulo(Figura):
    def __init__(self, **argumentos):
        argumentos['tipo'] = 'Triangulo'
        Figura.__init__(self,**argumentos)
        self.altura = argumentos.get('Altura')
        self.base = argumentos.get('Base')
    def imprime_argumentos(self):
        return 'Tipo: {}\nArea: {}'.format(self.tipo,(self.base*self.altura)/2).strip()

class Rectangulo(Figura):
    def __init__(self, **argumentos):
        argumentos['tipo'] = 'Rectangulo'
        Figura.__init__(self,**argumentos)
        self.base = argumentos.get('Base')
        self.altura = argumentos.get('Altura')

    def imprime_argumentos(self):
        return 'Tipo: {}\nArea: {}'.format(self.tipo,(self.base*self.altura)).strip()

class FigurasFactory():
    @staticmethod
    def crea_figura(**atributos):
        Figura = atributos.get('Figura')
        if atributos.get('Tipo') == 'Circulo':
            return Circulo(**atributos)
        elif atributos.get('Tipo') == 'Triangulo':
            return Triangulo(**atributos)
        elif atributos.get('Tipo') == 'Rectangulo':
            return Rectangulo(**atributos)
        else:
            return 'La Figura {} no existe'.format(Figura)

def main():
    figura1 = FigurasFactory.crea_figura(Tipo='Circulo', Radio=3)
    print(figura1.imprime_argumentos(),'\n')

    figura2 = FigurasFactory.crea_figura(Tipo='Triangulo', Base=3, Altura=4)
    print(figura2.imprime_argumentos(),'\n')

    figura3 = FigurasFactory.crea_figura(Tipo='Rectangulo', Base=7, Altura=5)
    print(figura3.imprime_argumentos(),'\n')

    figura4 = FigurasFactory.crea_figura(Tipo='Circulo', Radio=8)
    print(figura4.imprime_argumentos(),'\n')

    figura5 = FigurasFactory.crea_figura(Tipo='Rectangulo', Base=10, Altura=4)
    print(figura5.imprime_argumentos())

if __name__ == '__main__':
    main()