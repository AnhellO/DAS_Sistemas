class Calculadora(object):
    """docstring for Calculadora"""
    memoria = 10

    def set_memoria(self, memoria):
        self.memoria = memoria

    def suma(self,a, b):
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
print(calc.numerosPrimos(100))

print(calc.suma(calc, 2, 4))


class proxy (Calculadora):
    memoria=5
    

    def division_proxy(self,a,b):
        if b == 0:
            return 'operacion invalida'
        else:
            return Calculadora.division(Calculadora,a,b)

    def numerosPrimos(self, limite, maxMostrar):
        rango = range(2, limite)
        return [primo for primo in rango if sum(primo % num == 0 for num in rango) < 2][:maxMostrar]
        
    

calc = proxy
print(calc.division_proxy(calc,9,0))
print(calc.numerosPrimos(calc,100,16))
