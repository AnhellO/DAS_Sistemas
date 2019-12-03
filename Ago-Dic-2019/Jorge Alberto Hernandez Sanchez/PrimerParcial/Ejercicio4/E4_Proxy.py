class Calculadora(object):
	"""docstring for Calculadora"""
	memoria = 10

	def suma(self, a, b):
		return a + b

	def resta(self, a, b):
		return a - b

	def multiplicacion(self, a, b):
		return a * b

	def division(self, a, b):
		return a / b

	@classmethod
	def numerosPrimos(cls, limite):
		rango = range(2, limite)
		return [primo for primo in rango if sum(primo % num == 0 for num in rango) < 2][:cls.memoria]

calc = Calculadora
print(calc.division(calc, 0,5))
print(calc.numerosPrimos(100))


class Proxy():
	def __init__(self):
		self.__Calculadora = Calculadora()
	def suma(self, a,b):
		return a + b
	def resta(self, a, b):
		return a - b
	def multiplicacion(self, a, b):
		return a * b
	def division(self, a, b):
		if b == 0:
			return 0
		elif b > 0 or b < 0:
    			return a / b

calc2 = Proxy
print(calc2.division(calc,5,0))