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

    def salir(self):
        print("Apagando...")

    def apaga_pantalla(self):
        print("Se apaga pantalla")

    def reiniciar(self):
        print("Reiniciando...")


class ComputadoraMethFacade:

    def __init__(self, marca, componentes):
        self.computadora = Computadora(marca, componentes)

    #Comenzamos con las operaciones que tendra nuestro equipo. Cada una de estas operaciones tiene su funcion
    #por ejemplo self.computadora.inicializa()
    def encender(self):
        print("Encendiendo computadora...\n")
        self.computadora.presiona_boton()
        self.computadora.manda_luz()
        self.computadora.haz_sonido()
        self.computadora.inicializa()
        self.computadora.notifica()

    def apagar(self):
        print("Apagando computadora...\n")
        self.computadora.salir()
        self.computadora.haz_sonido()
        self.computadora.apaga_pantalla()
        self.computadora.presiona_boton()


    def reiniciar(self):
        print("Reiniciando computadora...\n")
        self.computadora.reiniciar()
        self.computadora.haz_sonido()
        self.computadora.apaga_pantalla()
        self.computadora.manda_luz()
        self.computadora.haz_sonido()
        self.computadora.inicializa()
        self.computadora.notifica()
        pass

    def func(self, do):
        self.encender() if do.get('encender') else "Fallo de operacion de encendido"
        self.apagar() if do.get('apagar') else "Fallo de operacion de apagado"
        self.reiniciar() if do.get('reiniciar') else "Fallo de operacion de reinicio"

def main():
    marca='HP'
    componentes=['RAM 4GB','OS 64bits']
    do = { 'encender': False, 'apagar': True, 'reiniciar': True }
    facade = ComputadoraMethFacade(marca, componentes)
    facade.func(do)


if __name__ == "__main__":
    main()