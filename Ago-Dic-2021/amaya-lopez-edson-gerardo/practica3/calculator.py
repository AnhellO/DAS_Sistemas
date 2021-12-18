from math import pow

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        return self.a + self.b

    def resta(self) -> int:
        return self.a - self.b

    def multriplicacion(self) ->int:
        return self.a * self.b

    def divicion(self) ->int:
        if self.b ==0:
            return 'el diviendo no debe ser 0'
        return self.a / self.b

    def potencia(self) -> int:
        return pow(self.a, self.b)

    def raiz(self)-> int:
        if self.a < 0:
            return 'no se puede sacar la raiz negativa'
        return pow(self.a,(1/self.b))



