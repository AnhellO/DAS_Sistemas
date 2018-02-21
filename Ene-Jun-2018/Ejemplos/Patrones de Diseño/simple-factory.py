from abc import ABC, abstractmethod

class Instrumento(object):

    def __init__(self, **atributos):
        self.tipo = atributos['tipo']
        self.madera = atributos['madera']
        self.color = atributos['color']

    @abstractmethod
    def suena_instrumento(self):
        pass


class Guitarra(Instrumento):

    def __init__(self, **atributos):
        atributos['tipo'] = 'cuerdas'
        super().__init__(atributos)
        self.orientacion = atributos['orientacion']
        self.cuerdas = atributos['cuerdas']

    def suena_instrumento(self):
        print('Wiriwiriwu')


class Bateria(Instrumento):

    def __init__(self, **atributos):
        atributos['tipo'] = 'percusion'
        print(atributos)
        super().__init__(atributos)
        self.piezas = piezas

    def suena_instrumento(self):
        print('Tupa tupa ba dum tsss!')

class InstrumentosFactory():

    @staticmethod
    def crea_instrumento(madera, color, orientacion, cuerdas, piezas, instrumento='guitarra'):
        if instrumento.lower() == 'guitarra':
            return Guitarra(madera, color, orientacion, cuerdas)
        elif instrumento.lower() == 'bateria':
            return Bateria(madera, color, piezas)
        else:
            print('El instrumento {} no existe'.format(instrumento))

bateria = Bateria(madera='roble', color='rojo', piezas=15)
guitarra = Bateria(madera='nogal', color='verde', cuerdas=6)

print(bateria.suena_instrumento())
print(guitarra.suena_instrumento())

#print(InstrumentosFactory.crea_instrumento('maple', 'rojo', 'zurdo', ).suena_instrumento())
