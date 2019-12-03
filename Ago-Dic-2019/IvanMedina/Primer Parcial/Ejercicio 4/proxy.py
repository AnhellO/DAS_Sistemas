
class Calculadora(object):
	"""docstring for Calculadora"""
	memoria = 10

	def suma(a, b):
		return a + b

	def resta(a, b):
		return a - b

	def multiplicacion(a, b):
		return a * b
	@classmethod
	def division(cls,a, b):
		return a / b

	@classmethod
	def numerosPrimos(cls, limite):
		rango = range(2, limite)
		return [primo for primo in rango if sum(primo % num == 0 for num in rango) < 2][:cls.memoria]
class Proxy:
   def __init__( self, subject ):
      self._subject = subject
      self._proxystate = None

class ProxyCalc( Proxy ):
	def numerosPrimos(self,limite ):
		primos=self._subject.numerosPrimos(100)
		#self._proxystate = 1
		return primos

	def division(self,a,b ):
	    if self._proxystate == None:
		    division=self._subject.division(a,b)
		    self._proxystate = 1
		    return division
	    return 'none'

if __name__ == '__main__':
	print("NUMEROS PRIMOS SIN PROXY...")
	calc1 = Calculadora
	print(calc1.numerosPrimos(100))

	print("DIVISION SIN PROXY...")
	calc1 = Calculadora
	try:
	    print(calc1.division(0,0))
	except:
		print("Error al dividir entre 0")

	print("NUMEROS PRIMOS CON PROXY...")
	calc2 = ProxyCalc(Calculadora)
	print(calc2.numerosPrimos(100))
	print("DIVISION CON PROXY...")
	try:
		print(calc2.division(0,0))
	except:
		print("Error al dividir entre 0")
