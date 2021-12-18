from typing import Match
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

    def division(self) -> float:
        if (self.b == 0):
            return "No se puede dividir entre cero"
        else:
            return self.a / self.b

    def potencia (self) -> int:
        return self.a ** self.b

    def raiz (self) -> float:
        if (self.a < 0):
            return "No se aceptan números negativos para la raíz cuadrada"
        else:
            return (self.b * (math.sqrt(self.a)))