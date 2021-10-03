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
        if self.b != 0:
            return self.a / self.b
        return "error"
    
    def potencia(self) -> int:
        return self.a ** self.b
        
    def raiz(self) -> int:
        if self.a != -1:
            return self.a ** (1/self.b)
        return "error"
