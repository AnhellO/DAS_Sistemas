class Calculadora(object):
	"""docstring for Calculadora"""
	memoria = 10

	def suma(a, b):
		return a + b

	def resta(a, b):
		return a - b

	def multiplicacion(a, b):
		return a * b

	def division(a, b):
		return a / b

	@classmethod
	def numerosPrimos(cls, limite):
		rango = range(2, limite)
		return [primo for primo in rango if sum(primo % num == 0 for num in rango) < 2][:cls.memoria]

calc = Calculadora
print(calc.numerosPrimos(100))