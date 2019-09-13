from abc import ABC, abstractmethod

class Instrumento(object):

    def __init__(self, **atributos):
        self.tipo = atributos.get('tipo')
        self.madera = atributos.get('madera')
        self.color = atributos.get('color')

    @abstractmethod
    def imprime_atributos(self):
        pass


class Guitarra(Instrumento):

    def __init__(self, **atributos):
        atributos['tipo'] = 'cuerdas'
        super().__init__(**atributos)
        self.orientacion = atributos.get('orientacion')
        self.cuerdas = atributos.get('cuerdas', 6)

    def imprime_atributos(self):
        return 'Tipo: {}\nCuerdas: {}\nMadera: {}\nColor: {}\nOrientacion: {}\n'.format(
            self.tipo,
            self.cuerdas,
            self.madera,
            self.color,
            self.orientacion
        )


class Bateria(Instrumento):

    def __init__(self, **atributos):
        atributos['tipo'] = 'percusion'
        super().__init__(**atributos)
        self.piezas = atributos.get('piezas', 1)

    def imprime_atributos(self):
        return 'Tipo: {}\nPiezas: {}\nMadera: {}\nColor: {}\n'.format(
            self.tipo,
            self.piezas,
            self.madera,
            self.color
        )


class InstrumentosFactory():

    @staticmethod
    def crea_instrumento(**atributos):
        instrumento = atributos.get('instrumento')
        if instrumento.lower() == 'guitarra':
            return Guitarra(**atributos)
        elif instrumento.lower() == 'bateria':
            return Bateria(**atributos)
        else:
            return 'El instrumento {} no existe'.format(instrumento)



bateria = Bateria(madera='roble', color='rojo', piezas=15)
guitarra = Guitarra(madera='nogal', color='verde', cuerdas=7, orientacion='zurdo')

print(bateria.imprime_atributos())
print(guitarra.imprime_atributos())

instrumento_1 = InstrumentosFactory.crea_instrumento(instrumento='guitarra', madera='maple', color='rojo', orientacion='zurdo')
print(instrumento_1.imprime_atributos())
instrumento_2 = InstrumentosFactory.crea_instrumento(instrumento='bateria', madera='roble', color='negro')
print(instrumento_2.imprime_atributos())
instrumento_3 = InstrumentosFactory.crea_instrumento(instrumento='bajo')
print(instrumento_3)