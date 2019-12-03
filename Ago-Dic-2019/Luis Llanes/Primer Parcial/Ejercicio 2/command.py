from abc import ABCMeta, abstractmethod

# Receiver
class Television(object):
    """docstring for Television"""
    def encender(self):
        print('Encendida!')

    def apagar(self):
        print('Apagada!')

    def cambiarCanal(self, numCanal):
        print('Cambiamos al canal {}'.format(numCanal))

    def subirVolumen(self):
    	print('Subimos volumen!')

    def bajarVolumen(self):
        print('Bajamos volumen!')


@abstractmethod
class ControlRemoto(object):
    """docstring for ControlRemoto"""
    def accion(self, comando):
        return 'television.'+comando
		



tv = Television()
tv.encender()

control = ControlRemoto()
control.accion('bajarVolumen')