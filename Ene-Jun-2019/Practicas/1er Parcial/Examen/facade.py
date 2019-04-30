class Componente(object):
    """docstring for Componente"""
    def __init__(self, nombre=''):
        self.nombre = nombre

    def __str__(self):
        return 'Componente: {}'.format(self.nombre)

class Computadora(object):
    """docstring for Computadora"""

    componentes = []

    def __init__(self, marca, componentes=[]):
        self.marca = marca
        self.componentes = [Componente(i) for i in componentes]

    def __str__(self):
        return 'Computadora marca: {}\nEspecificaciones: {}'.format(self.marca, '\n'.join([str(i) for i in self.componentes]))

    def set_componente(self, componente):
        self.componentes.append(Componente(componente))

    def presiona_boton(self):
        print('Click!')

    def manda_luz(self):
        print('Pzzzzzzzt!')

    def haz_sonido(self):
        print('Beep Beep!')

    def inicializa(self):
        print('Inicializando componentes...\n' + '\n'.join([str(i) for i in self.componentes]))

    def notifica(self):
        print('Listo!')