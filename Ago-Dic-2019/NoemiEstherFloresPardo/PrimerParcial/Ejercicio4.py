"""Ejercicio 4 - Proxy Command
Para el ejemplo de código en el archivo proxy.py:
Implementa la funcionalidad necesaria utilizando el patrón de diseño Proxy para que sea posible llevar a cabo las operaciones de la clase Calculadora por medio del proxy
division(): valida la división entre 0
numerosPrimos(): permite que sea posible obtener más números primos en base a una memoria dinámica dentro del objeto Proxy"""


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

calc = Calculadora
print(calc.numerosPrimos(100))