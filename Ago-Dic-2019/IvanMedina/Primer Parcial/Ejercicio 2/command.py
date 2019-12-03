#receiver
class Television(object):
	"""docstring for Television"""
	def encender():
		print('Encendida!')

	def apagar():
		print('Apagada!')

	def cambiarCanal(numCanal):
		print('Cambiamos al canal'.format(numCanal))

	def subirVolumen():
		print('Subimos volumen!')

	def bajarVolumen():
		print('Bajamos volumen!')


class ControlRemoto(object):
	"""docstring for ControlRemoto"""
	def accion(comando):
		pass
		

tv = Television()
tv.encender()


control = ControlRemoto
control.accion(comando)
