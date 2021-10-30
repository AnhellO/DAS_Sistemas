class Calculadora:

    def __init__(self, a : int, b : int) -> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        resultado = self.a + self.b    
        return resultado

    def resta(self) -> int:
        resultado = self.a - self.b    
        return resultado

    def multiplicacion(self) -> int:
        resultado = self.a * self.b    
        return resultado

    def division(self):
        if self.b <= 0:
            errorMessage = 'No se puede dividir entre cero'
            return errorMessage
        resultado = self.a / self.b, 2
        return resultado


    def potencia(self) -> int:
        resultado = self.a ** self.b    
        return resultado


if __name__ == '__main__':
    pass 
