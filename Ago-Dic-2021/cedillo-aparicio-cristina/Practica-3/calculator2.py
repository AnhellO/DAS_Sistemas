from typing import Match
import math

class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def suma(a,b) -> int:
        return a + b

    def resta(a,b) -> int:
        return a - b

    def multiplicacion(a,b) -> int:
        return a * b

    def division(a,b) -> float:
        if (b == 0):
            return "No se puede dividir entre cero"
        else:
            return a / b

    def potencia (a,b) -> int:
        return a ** b

    def raiz (a,b) -> float:
        if (a < 0):
            return "No se aceptan numeros negativos para la raiz cuadrada"
        else:
            return (b * (math.sqrt(a)))