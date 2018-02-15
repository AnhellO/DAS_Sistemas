from abc import ABC, abstractmethod

class Instrumento:

    def __init__(self, tipo, madera, color):
        self.tipo = tipo
        self.madera = madera
        self.color = color

    @abstractmethod
    def suena_instrumento(self):
        pass

    @abstractmethod
    def imprime_atributos(self):
        pass


class Guitarra(Instrumento):

    def __init__(self, tipo, madera, color, orientacion, cuerdas=6):
        super().__init__(tipo, madera, color)
        self.orientacion = orientacion
        self.cuerdas = cuerdas

    def get_num_cuerdas(self):
        return self.cuerdas

    def suena_instrumento(self):
        print('Wiriwiriwu')

    def imprime_atributos(self):
        print('Tipo: {}\nCuerdas: {}\nMadera: {}\nColor: {}\nOrientacion: {}'.format(
            self.tipo,
            self.cuerdas,
            self.madera,
            self.color,
            self.orientacion
        ))

class Bateria(Instrumento):

    def __init__(self, tipo, madera, color, piezas):
        super().__init__(tipo, madera, color)
        self.piezas = piezas

    def suena_instrumento(self):
        print('Tupa tupa ba dum tsss!')

    def imprime_atributos(self):
        print('Foto de la batería aquí')
