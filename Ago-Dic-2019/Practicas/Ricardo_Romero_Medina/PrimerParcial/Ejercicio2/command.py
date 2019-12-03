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
