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
        if self.a == 0 or self.b == 0:
            return 0
        else:
            return self.a / self.b

    def potencia(self) -> int:
        return self.a ** self.b

    def raiz(self) -> int:
        if self.a < 0:
            return 0
        else:
            return round(self.a ** (1 / self.b))
        