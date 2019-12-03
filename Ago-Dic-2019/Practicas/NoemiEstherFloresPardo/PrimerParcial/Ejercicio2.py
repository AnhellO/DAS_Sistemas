"""Ejercicio 2 - Pattern Command
Para el ejemplo de código en el archivo command.py:
Implementa la funcionalidad necesaria utilizando el patrón de diseño Command para poder llevar a cabo cada de unas de las acciones de la televisión
por medio de la clase ControlRemoto
Ejemplo al encender la televisión: Encendida!
De acuerdo al patrón de diseño Command, debemos de tener la posibilidad de deshacer la acción realizada. Implementa la funcionalidad necesaria para poder
deshacer cada acción llevada a cabo con la televisión"""

#Receiver
class Television(object):
    """docstring for Television"""
    def encender(self):
        print('Encendida!')

    def apagar(self):
        print('Apagada!')

    def cambiarCanal(self,numCanal):
        print('Cambiamos al canal {}'.format(numCanal))

    def subirVolumen(self):
        print('Subimos volumen!')

    def bajarVolumen(self):
        print('Bajamos volumen!')

#CONCRETE COMMANDS
class encender(Television):
    def encender(self,Television):
        return Television.encender()

class apagar(Television):
    def apagar(self,Television):
        return Television.apagar()

class cambiarCanal(Television):
    def cambiarCanal(self,Television):
        return Television.cambiarCanal()

class subirVolumen(Television):
    def subirVolumen(self,Television):
        return Television.subirVolumen()

class bajarVolumen(Television):
    def bajarVolumen(self,Television):
        return Television.bajarVolumen()


class ControlRemoto(object):
    def accion(self,comando):
        if comando == 'encender':
            encender()
        #comando.apagar()
        #comando.cambiarCanal()
        #comando.subirVolumen()
        #comando.bajarVolumen()


#tv = Television()
#tv.encender()

control = ControlRemoto()
control.accion('encender')