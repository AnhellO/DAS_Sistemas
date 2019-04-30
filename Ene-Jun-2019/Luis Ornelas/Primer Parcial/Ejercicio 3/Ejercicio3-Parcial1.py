import time

SLEEP = 1

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
class Encender:
    def encender(self):
        # Preciona Boton
        print('---Encender---\nClick!')
        time.sleep(SLEEP)
        # Luz
        print('Pzzzzzzzt!')
        time.sleep(SLEEP)
        # Sonidos
        print('Beep Beep!')
        time.sleep(SLEEP)
        # Inicializando
        print('Inicializando componentes...')
        time.sleep(SLEEP)
        # Notificacion
        print('Listo!')
        time.sleep(SLEEP)
class Apagar:
    def apagar(self):
        # Preciona Boton
        print('---Apagar---\nClick!')
        time.sleep(SLEEP)
        # Asegurando que las aplicaciones esten listas para cerrar
        print('Apagando...')
        time.sleep(SLEEP)
        # Finalizando Componentes
        print('Finalizando Componentes...')
        time.sleep(SLEEP)
        # Sonido de Windows XP
        print('Turururu')
        time.sleep(SLEEP)
        # Pantalla
        print('Pzz Showt')
        time.sleep(SLEEP)
class Reiniciar:
    def reiniciar(self):
        # Preciona Boton
        print('---Reiniciar---\nClick!')
        time.sleep(SLEEP)
        # Asegurando que las aplicaciones esten listas para cerrar
        print('Apagando...')
        time.sleep(SLEEP)
        # Finalizando Componentes
        print('Finalizando Componentes...')
        time.sleep(SLEEP)
        # Sonido
        print('Turururu')
        time.sleep(SLEEP)
        # Pantalla
        print('Pzz Showt')
        time.sleep(SLEEP)
        # Luz
        print('Pzzzzzzzt!')
        time.sleep(SLEEP)
        # Sonidos
        print('Beep Beep!')
        time.sleep(SLEEP)
        # Inicializando
        print('Inicializando componentes...')
        time.sleep(SLEEP)
        # Notificacion
        print('Listo!')
        time.sleep(SLEEP)

class Facade:

    def __init__(self, tests={}):
        self.encender = Encender() if tests.get('Encender') else None
        self.apagar = Apagar() if tests.get('Apagar') else None
        self.reiniciar = Reiniciar() if tests.get('Reiniciar') else None

    def runOperaciones(self):
        self.encender.encender() if self.encender else print('Ya esta Encendida')
        self.apagar.apagar() if self.apagar else print('Ya esta Apagada')
        self.reiniciar.reiniciar() if self.reiniciar else print('No hay necesidad de Reiniciar')

compus = {
    'Encender': True,
    'Apagar': True,
    'Reiniciar': True
}

operaciones = Facade(compus)
operaciones.runOperaciones()
