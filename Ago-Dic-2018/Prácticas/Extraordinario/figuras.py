class Rectangulo(object):
    def set_altura(self, altura):
        self.altura = altura
        return self

    def set_base(self, base):
        self.base = base
        return self

    def area(self):
        return self.base * self.altura


class GeneradorGraficos(object):
    def __init__(self, rectangulo = None):
        self.rectangulo = rectangulo

    def set_rectangulo(self, rectangulo):
        self.rectangulo = rectangulo
        return self

    def dibujar_rectangulo(self):
        return self.rectangulo.area()


if __name__ == '__main__':
    rectangulo = Rectangulo()
    rectangulo.set_altura(4).set_base(2)

    cuadrado = Rectangulo()
    cuadrado.set_altura(5).set_base(5)

    generador_de_graficos = GeneradorGraficos(rectangulo)
    print(generador_de_graficos.dibujar_rectangulo())

    generador_de_graficos.set_rectangulo(cuadrado)
    print(generador_de_graficos.dibujar_rectangulo())