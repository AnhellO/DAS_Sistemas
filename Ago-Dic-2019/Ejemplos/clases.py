


class Automovil:
	"""docstring for Automovil"""
	def __init__(self, **argumentos):
		self._color = argumentos.get('color')
		self._marca = argumentos.get('marca')
		self._modelo = argumentos.get('modelo', '')

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def set_marca(self, marca):
		self._marca = marca

	def get_marca(self):
		return self._marca

	def set_modelo(self, modelo):
		self._modelo = modelo

	def get_modelo(self):
		return self._modelo

	def distribuidores(self, *distribuidores):
		print(distribuidores[0])
		print(distribuidores[1])
		print(distribuidores[2])
		return distribuidores

	def __str__(self):
		return '''
			Color: {}\nMarca: {}\nModelo: {}
		'''.format(self._color, self._marca, self._modelo).strip()

auto = Automovil(
	color='rojo',
	marca='chevrolet'
)
print(auto)
# auto._color = 'verde' -> No es el correcto
# auto.set_color('verde')
# print(auto.distribuidores('autozone', 'lotes de auto chachito', 'uadec', 4))


