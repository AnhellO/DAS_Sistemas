import math

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        return self.a + self.b

    def resta(self) -> int:
        return self.a - self.b

    def multiplicacion(self) -> int:
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return ('ZeroDivisionError: division by zero')

    def potencia(self) -> int:
        return math.pow(self.a, self.b)

    def raiz(self) -> int:
        if self.a == 0 or self.b == 0:
            return("Sin Definir")
        elif(self.a < 0):
            return "Imposible Raiz de un Negativo"
        else:
            return(self.a ** 1/self.b)


if __name__ == "__main__":

    calculadora = Calculator(100, 0)
    print(calculadora.suma())
    print(calculadora.resta())
    print(calculadora.multiplicacion())
    print(calculadora.division())
    print(calculadora.potencia())
    print(calculadora.raiz())