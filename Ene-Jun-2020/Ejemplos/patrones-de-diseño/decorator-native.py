########################################
##### Decoradores nativos de Python
########################################

# 1: Funciones como objetos y referencias

def hello_world():
	return 'Hola Mundo!'

def hello_world_with_name(function, name):
	return f'{function()}, y hola {name}!'

print(hello_world_with_name(hello_world, 'Bobby'))

# 2: Funciones internas

def hello_class():
	print('Hola clase de diseño y arquitectura de software!')

	def hello_emilio():
		print('y hola a ti Emilio :D!')

	def hello_angela():
		print('y hola a ti Angela :D!')

	def hello_fer():
		print('y hola a ti Luis Fernando >:D!')

	hello_emilio()
	hello_angela()
	hello_fer()

hello_class()

# 3: Podemos retornar valores desde las funciones internas

def hello_class(numero):
	print('Hola clase de diseño y arquitectura de software!')

	def hello_emilio():
		return 'y hola a ti Emilio :D!'

	def hello_angela():
		return 'y hola a ti Angela :D!'

	def hello_fer():
		return 'y hola a ti Luis Fernando >:D!'

	if numero == 1:
		return hello_emilio()

	if numero == 2:
		return hello_angela()

	if numero == 3:
		return hello_fer()

print(hello_class(1))
variable = hello_class(2)
print(variable)

# 4: Ahora si los decorators! :D

def cafecito():
	print('Cafecito! :D')

def decorador(function):
	def wrapper():
		function()
		print('Con pan!')
		print('Y con leche y azúcar >:D!')

	return wrapper

cafecito = decorador(cafecito)
print(cafecito())

# 5: Decoradores con "syntactic sugar" ;) wink-wink

def decorador(function):
	def wrapper():
		function()
		print('Con pan!')
		print('Y con leche y azúcar >:D!')

	return wrapper

@decorador
def cafecito():
	print('Cafecito! :D')

print(cafecito())