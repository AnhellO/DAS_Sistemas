# Para el ejemplo de código en el archivo facade.py:
# Implementa la funcionalidad necesaria utilizando el patrón de diseño
# Facade para poder prender, apagar, y reiniciar una instancia de la clase
# Computadora
# Ejemplo al prender la computadora:
# Click!
# Pzzzzzzzt!
# Beep Beep!
# Inicializando componentes...
# ...
# Listo!
# Explica la lógica implementada detrás de tu enfoque

class Componente(object):
    """docstring for Componente"""
    def __init__(self, nombre=''):
        self.nombre = nombre

    def __str__(self):
        return 'Componente: {}'.format(self.nombre)

class Computadora(object):
    """docstring for Computadora"""

    componentes = []

    # Constructor de computadora
    def __init__(self, marca, componentes=[]):
        self.marca = marca
        self.componentes = [Componente(i) for i in componentes]

    # Mostrar marca y especificaciones de la computadora
    def __str__(self):
        return 'Computadora marca: {}\nEspecificaciones: {}'.format(self.marca, '\n'.join([str(i) for i in self.componentes]))

    def set_componente(self, componente): # agregar componentes
        self.componentes.append(Componente(componente))

    # funciones computadora
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

    # método agregado para notificar al usuario que la compu está por apagarse
    def apagada(self):
        print('A punto de apagarse')

    # Método agregado para reiniciar la computadora, click con el mouse a "reiniciar"
    def click_reiniciar(self):
        print('A punto de reiniciar...')

class Facade(object):
    def __init__(self):
        self._compu = Computadora("HP",["a"]) # creamos instancia de computadora

    def prenderCompu(self):
        # función para prender la computadora con los métodos ejecutados al prenderla
        self._compu.presiona_boton()
        self._compu.manda_luz()
        self._compu.haz_sonido()
        self._compu.inicializa()
        self._compu.notifica()

    def apagarCompu(self):
        # función para apagar la computadora con un solo método ejecutado para apagarla
        # solo click en el botón apagar y listo!
        self._compu.presiona_boton()
        self._compu.apagada()

    def reiniciarCompu(self):
        # función para reiniciar la computadora con varios métodos tal como click en
        # "reiniciar", después notifica al usuario que está por apagarse
        self._compu.click_reiniciar()
        self._compu.apagada() # computadora a punto de apagarse
        self._compu.manda_luz() # empieza a iniciarse después de apagarse
        self._compu.haz_sonido()
        self._compu.inicializa()
        self._compu.notifica()

    def prender_apagar_reiniciar(self):
        print("PRENDER COMPU")
        self.prenderCompu()
        print("\nAPAGAR COMPU")
        self.apagarCompu()
        print("\nREINICIAR COMPU")
        self.reiniciarCompu()

# Explicación: El objetivo de este patrón es reducir la complejidad
# del entorno con la división en subsistemas, en este caso los subsistemas son:
# prenderCompu(), reiniciarCompu() y prender_apagar_reiniciar(), que

def main():
    facade = Facade()
    facade.prender_apagar_reiniciar()

if __name__ == "__main__":
    main()
