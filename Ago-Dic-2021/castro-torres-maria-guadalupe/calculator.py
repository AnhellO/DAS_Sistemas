import math

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b

    def multiplicacion(self)->int:
        return self.a * self.b 

    def division(self)->int:
        if self.b == 0:
            return "El divisor no puede ser cero"
        else:
          return self.a / self.b    


    def potencia(self)->int:
        return pow(self.a , self.b )

    def raiz(self)->int:
        if self.a < 0:
            return "No se puede calcular la raiz de numeros negativos"
        else:    
         return (self.b * (math.sqrt(self.a)))       