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

class calproxy():

    def divisiont(a,b):
        if b == 0:
            return "No se puede efectuar la division"
        else:
            return Calculadora.division(a,b)


calc = Calculadora
print(calc.numerosPrimos(100))


cal = calproxy
print(cal.divisiont(3,0))




