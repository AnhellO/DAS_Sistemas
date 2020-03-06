class Computer(object):
	"""docstring for Computer"""
	def __init__(self, **args):
		self.procesador = args.get('procesador')
		self.memoria = args.get('memoria')
		self.tarjeta_video = args.get('tarjeta_video')
		
	def set_procesador(self, procesador):
		self.procesador = procesador

	def get_procesador(self):
		return self.procesador

	def set_memoria(self, memoria):
		self.memoria = memoria

	def get_memoria(self):
		return self.memoria

	def set_tarjeta_video(self, tarjeta_video):
		self.tarjeta_video = tarjeta_video

	def get_tarjeta_video(self):
		return self.tarjeta_video

	def __str__(self):
		return f'##### Mi Compu #####\nProcesador: {self.procesador}\nMemoria: {self.memoria}\nTarjeta de Vidio: {self.tarjeta_video}'

	def obtener_energia(self):
		return f'Ya tengo el poder para mi procesador {self.procesador} >:D!'

	def hacer_sonidito(self):
		return 'Pi pi pi pi pssssss'

	def iniciar_sistema(self):
		return f'Pero tengo windows y mi memoria {self.memoria} no la arma :(!'

	def carga_pantalla(self):
		return f'Windows v1000 con gráficos {self.tarjeta_video}'

	def cierra_apps(self):
		return 'Cerrando programas...'

	def cierra_sesion(self):
		return 'Usuario Pepito ha abandonado!'

	def deten_componentes(self):
		return f'Apagando procesador: {self.procesador}, memoria: {self.memoria} y vidio: {self.tarjeta_video}'

	def apagate(self):
		return 'Estoy apagao >:(!'

class ComputerFacade(object):
	"""docstring for ComputerFacade"""
	def __init__(self):
		self._pc = Computer(procesador='Intel i7 Generación 5', memoria='128MB', tarjeta_video='Nvidia GForce')

	def prender_compu(self):
		print(self._pc.obtener_energia())
		print(self._pc.hacer_sonidito())
		print(self._pc.carga_pantalla())
		print(self._pc.iniciar_sistema())

	def apagar_compu(self):
		print(self._pc.cierra_sesion())
		print(self._pc.cierra_apps())
		print(self._pc.deten_componentes())
		print(self._pc.apagate())

def main():
	facade = ComputerFacade()
	facade.prender_compu()
	facade.apagar_compu()


if __name__ == "__main__":
    main()