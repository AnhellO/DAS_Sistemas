########################################
##### Decoradores nativos de Python
########################################

print(f"\n{'#'*10} 1: Funciones como objetos y referencias {'#'*10}")

def hello_world():
	return 'Hola Mundo!'

def hello_world_with_name(function, name):
	return f'{function()}, y hola {name}!'

print(hello_world_with_name(hello_world, 'Bobby'))

print(f"\n{'#'*10} 2: Funciones internas {'#'*10}")

def hello_class():
	print('Hola clase de diseño y arquitectura de software!')

	def hello_you():
		print('\ty hola a ti que me estás viendo desde la pantalla >:D!')

	hello_you()

hello_class()

print(f"\n{'#'*10} 3: Podemos retornar valores desde las funciones internas {'#'*10}")

def hello_class_2(num):
	my_string = 'Hola clase de diseño y arquitectura de software!'

	def hello_you(num):
		return f'\ty a ti también que me estás viendo desde la pantalla >:D! {num}'

	def hello_there():
		return '\ty a ti también que no me estás viendo desde la pantalla >:C!'

	if num == 1:
		return f'{my_string}\n{hello_you(10)}'

	if num == 2:
		return f'{my_string}\n{hello_there()}'

print(hello_class_2(1))
# print(hello_you(1)) -> Esto dará error ya que hello_you existe solamente en el contexto/ámbito (scope) de la función hello_class_2
variable = hello_class_2(2)
print(variable)
print(hello_class_2(3))

print(f"\n{'#'*10} 4: Ahora si los decorators nativos {'#'*10}")

def cafecito():
	print('Cafecito! :D')

def decorador(function):
	def wrapper():
		print('Hehehe')
		function()
		print('Con pan!')
		print('Y con leche y azúcar >:D!')

	return wrapper

x = decorador(cafecito)
cafecito()
x()

print(f"\n{'#'*10} 5: Decoradores con 'syntactic sugar' {'#'*10}")

def decorador(function):
	def wrapper():
		print('Hehehe')
		function()
		print('Con pan!')
		print('Y con leche y azúcar >:D!')

	return wrapper

@decorador
def cafecito():
	print('Cafecito! :D')

cafecito()