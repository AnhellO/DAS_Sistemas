import sys

# Funciones

def suma(a, b):
	return a + b

print(suma(2, 4))

def imprime_nombre(mensaje, nombre):
	print(f'{mensaje} {nombre}')

imprime_nombre('Un mensaje coqueto:', 'Juanito')

def division(x, y):
	if y == 0:
		return 0, 'División entre 0 no permitida!'

	return x / y

resultado, mensaje = division(10, 0)
print(resultado)
print(mensaje)

suma = lambda a, b: a + b
print(suma(2, 4))

# Formateando strings

nombre = 'Juanito'
nombre2 = 'Jose'
print('Hola ' + nombre)
print('Hola %s' % (nombre)) # Old style de Python 2
print('Hola {}'.format(nombre)) # Old style de Python >3.0 y <3.6
print('Hola {} y {}'.format(nombre, nombre2))
print(f'Hola {nombre}') # New style de Python >=3.6
print(f'Hola {nombre.upper()} y {nombre2.upper()}')

# Clases y Objetos

class Organizacion(object):
	"""docstring for Organizacion"""
	def __init__(self, **args):
		# print(args)
		# sys.exit(0)
		self.nombre = args.get('nombre')
		self.tipo = args.get('tipo', '')
		self.descripcion = args.get('descripcion')

	def set_nombre(self, nombre):
		self.nombre = nombre

	def get_nombre(self):
		return self.nombre
	
	def set_tipo(self, tipo):
		self.tipo = tipo

	def get_tipo(self):
		return self.tipo
	
	def set_descripcion(self, descripcion):
		self.descripcion = descripcion

	def get_descripcion(self):
		return self.descripcion

	# ejemplo protected
	def __ubicacion(self):
		return 'Tangamandapio'

	def __str__(self):
		return f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}'
		

organizacion1 = Organizacion(nombre='ONU', descripcion='paz mundial')
# organizacion1.set_tipo('global')
print(organizacion1)
# print(organizacion1.ubicacion())






















