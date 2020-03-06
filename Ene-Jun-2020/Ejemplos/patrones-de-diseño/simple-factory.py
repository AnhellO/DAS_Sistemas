class Vehiculo(object):
	"""docstring for Vehiculo"""
	def __init__(self, **args):
		self._color = args.get('color')
		self._modelo = args.get('modelo')
		self._marca = args.get('marca')
		
	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def set_modelo(self, modelo):
		self._modelo = modelo

	def get_modelo(self):
		return self._modelo

	def set_marca(self, marca):
		self._marca = marca

	def get_marca(self):
		return self._marca

	def __str__(self):
		return f'Color: {self._color}\nModelo: {self._modelo}\nMarca: {self._marca}\n'

class Automovil(Vehiculo):
	"""docstring for Automovil"""
	def __init__(self, **args):
		super(Automovil, self).__init__(**args)
		self._llantas = args.get('llantas')
		self._puertas = args.get('puertas')
		self._matricula = args.get('matricula')
		
	def set_llantas(self):
		self._llantas = llantas

	def get_llantas(self):
		return self._llantas

	def set_puertas(self, puertas):
		self._puertas = puertas

	def get_puertas(self):
		return self._puertas

	def set_matricula(self, matricula):
		self._matricula = matricula

	def get_matricula(self):
		return self._matricula

	def __str__(self):
		return f'{super(Automovil, self).__str__()}Llantas: {self._llantas}\nPuertas: {self._puertas}\nMatricula: {self._matricula}'

class Avion(Vehiculo):
	"""docstring for Avion"""
	def __init__(self, **args):
		super(Avion, self).__init__(**args)
		self._aerolinea = args.get('aerolinea')
		self._capacidad = args.get('capacidad')
		self._peso_maximo = args.get('peso_maximo')
		
	def set_aerolinea(self, aerolinea):
		self._aerolinea = aerolinea

	def get_aerolinea(self):
		return self._aerolinea

	def set_capacidad(self, capacidad):
		self._capacidad = capacidad

	def get_capacidad(self):
		return self._capacidad

	def set_peso_maximo(self, peso_maximo):
		self._peso_maximo = peso_maximo

	def get_peso_maximo(self):
		return self._peso_maximo

	def __str__(self):
		return f'{super(Avion, self).__str__()}Aerolínea: {self._aerolinea}\nCapacidad: {self._capacidad}\nPeso Máx.: {self._peso_maximo}'

class Barco(Vehiculo):
	"""docstring for Avion"""
	def __init__(self, **args):
		super(Barco, self).__init__(**args)
		self._ancla = args.get('ancla')
		self._categoria = args.get('categoria')
		
	def set_ancla(self, ancla):
		self._ancla = ancla

	def get_ancla(self):
		return self._ancla

	def set_categoria(self, categoria):
		self._categoria = categoria

	def get_categoria(self):
		return self._categoria

	def __str__(self):
		return f'{super(Barco, self).__str__()}Ancla?: {self._ancla}\nCategoría: {self._categoria}'

# cochecito = Automovil(llantas='Michelin', puertas=5, matricula='ASGD234D')
# cochecito.set_color('Rojo')
# cochecito.set_modelo(2020)
# cochecito.set_marca('Chevrolet')
# print(cochecito)

class VehiculoSimpleFactory(object):
	"""docstring for SimpleFactory"""

	@staticmethod
	def create(tipo: str, **args):
		tipo = tipo.lower()
		
		if tipo == 'automovil':
			return Automovil(**args)
		elif tipo == 'avion':
			return Avion(**args)
		elif tipo == 'barco':
			return Barco(**args)

		raise Exception(f'Tipo {tipo} invalido!')

auto = VehiculoSimpleFactory.create('automovil', llantas='Michelin', puertas=5, matricula='ASGD234D', color='Rojo', modelo=2020, marca='Chevrolet')
avion = VehiculoSimpleFactory.create('avion', aerolinea='Interjet', capacidad=1000, peso_maximo=1000.0, color='Rojo', modelo=2020, marca='Boeing')
barco = VehiculoSimpleFactory.create('Barco', ancla=True, categoria='Comercial', color='Rojo', modelo=2020, marca='Chevrolet')

print(auto)
print(avion)
print(barco)