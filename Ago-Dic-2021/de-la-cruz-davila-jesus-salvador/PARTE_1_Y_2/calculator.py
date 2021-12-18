class Calculator:
    # Funcion donde se definen las variables
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    # Funcion que suma los numeros
    def suma(self) -> int:
        return self.a + self.b

    # Funcion que resta los numeros
    def resta(self) -> int:
        return self.a - self.b

    # Funcion que multiplica los numeros
    def multiplicacion(self) -> int:
        return self.a * self.b

############################ PARTE 2 ##############################################

    # Funcion que divide los numeros
    def division(self) -> float:
        if self.b == 0:
            return "No es posible dividir entre 0"
        else:
            return self.a / self.b

    # Funcion de eleva a una potencia
    def potencia(self) -> int:
        if self.b == 0:
            return 1
        else:
            return self.a ** self.b

    # Funcion para sacar raiz
    def raiz(self) -> float:
        if self.a < 0:
            return "No se puede raiz negativa"
        elif self.a == 0:
            return 0
        else:
            return pow(self.a, (1/(self.b)))