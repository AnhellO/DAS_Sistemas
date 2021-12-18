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

    def division(self) -> int:
        if self.b == 0:
            return "No se puede dividir entre 0"
        else:
            return (self.a / self.b)

    def raizNumero(self) -> int:
        if self.a < 0:
            return "No se puede raiz de negativos"
        else:
            return pow(self.a, (1/(self.b)))

    def potencia(self) -> int:
        return pow(self.a, self.b)