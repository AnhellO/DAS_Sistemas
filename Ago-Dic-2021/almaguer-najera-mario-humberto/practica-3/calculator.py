class Calculator:

    def __init__(self, a : int, b : int) -> None:
        self.a = a
        self.b = b

    def suma(self) -> int:
        return self.a + self.b    
    
    def resta(self) -> int:
        return self.a - self.b

    def multiplicacion(self) -> int:
        return self.a * self.b

    def division(self):
        if self.b <= 0:
            #Nos regresa una cadena de texto si "b" es menor o igual a 0.
            return 'Error!, no se puede dividir entre cero o menor a cero.'
        #Se redondea la division a 2 decimales.
        return round(self.a / self.b, 2)
            

    def potencia(self) -> int:
        return self.a ** self.b

    def raiz(self) -> int:
        if self.a > 0:
            return self.a ** (1 / float(self.b))
        #Nos regresa una cadena de texto si el numero es negativo.
        return 'Error!, no se puede obtener la raiz de un numero negativo.'


if __name__ == '__main__':
    pass