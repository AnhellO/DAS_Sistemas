class Calculadora(object):
    """docstring for Calculadora"""
    memoria = 10
    def suma(self,a, b):
        return a + b

    def resta(self,a, b):
        return a - b

    def multiplicacion(self,a, b):
        return a * b

    def division(self,a, b):
        return a / b

    @classmethod
    def numerosPrimos(cls, limite):
        rango = range(2, limite)
        return [primo for primo in rango if sum(primo % num == 0 for num in rango) < 2][:cls.memoria]

class proxyCalculadora(Calculadora):
    def proxyDivision(self,a,b):
        if b == 0:
            return 'No se puede realizar la division'
        else:
            return Calculadora.division(Calculadora,a,b)

calc = proxyCalculadora
print(calc.proxyDivision(Calculadora,5,4))