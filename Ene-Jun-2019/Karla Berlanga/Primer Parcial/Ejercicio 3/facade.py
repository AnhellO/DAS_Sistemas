"""
Para el ejemplo de código en el archivo facade.py:
Implementa la funcionalidad necesaria utilizando el patrón de diseño Facade para poder prender, apagar, y reiniciar una instancia de la clase Computadora
Ejemplo al prender la computadora:
Click!
Pzzzzzzzt!
Beep Beep!
Inicializando componentes...
...
Listo!
Explica la lógica implementada detrás de tu enfoque
"""
#############Parte Compleja##################
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

#Facade : Es la interfaz de nivel superior que facilita el subsistema, para esta caso
#el subsistema es Computadora
class ComputadoraFacade:

    def __init__(self, marca, componentes):
        self.computadora = Computadora(marca, componentes)

    #En esta operación de la fachada encendemos la computadora
    #Como se puede notar, detras de todo esto esta la parte compleja
    #de la cual no tenemos conocimiento en este punto
    #pues esta es la funcion de este patron
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

    def operation(self, do):
        self.encender() if do.get('encender') else "No se prendió la computadora"
        self.apagar() if do.get('apagar') else "No se apagó la computadora"
        self.reiniciar() if do.get('reiniciar') else "No se reinició la computadora"


def main():
    marca='Dell'
    componentes=['RAM 8GB','OS 64bits']
    do = { 'encender': False, 'apagar': True, 'reiniciar': True }
    fachada = ComputadoraFacade(marca, componentes)
    fachada.operation(do)
    #fachada.encender()
    #print("\n")
    #fachada.reiniciar()
    #print("\n")
    #fachada.apagar()


if __name__ == "__main__":
    main()
