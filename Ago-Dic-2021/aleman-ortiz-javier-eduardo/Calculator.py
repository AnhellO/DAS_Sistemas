import math
class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b
    
    def Multiplicacion(self)-> int:
        return self.a * self.b

    def Division(self)-> int:
        if self.b == 0:
            return "Error"
        else:
            return self.a/self.b
    
    def Potencia(self)-> int:
        return pow(self.a, self.b)
    
    def Raiz(self)-> int:
        if self.a < 0:
            return "Error"
        else:
            return round(self.b*(math.sqrt(self.a)),8)