class calculator:
    #ingresamieno de 2 numeros
    def __init__(self,a : int ,b: int) -> None:
        self.a = a
        self.b = b

    #Suma de 2 numeros
    def Suma(self) -> int :
        return self.a + self.b 

    #Resta de numeros
    def Resta(self) -> int:
        return self.a - self.b

    #Multiplicacion de numeros
    def Multiplicacion(self) -> int :
        return self.a * self.b

    #Division de numeros
    def Division(self) -> int :
       if self.b == 0:
           return 0
       else:
           return self.a /self.b
        
    #Elevar un numero "A" a potencia "B"
    def Potencias(self) -> int :
        return self.a ** self.b

    #Sacar la raiz "B" de un numero "A"
    def Raiz(self) -> float :
        if self.a < 0:
            return None

        else:
            return self.a ** (1/self.b)

    #Hacer una calculadora mas simple para las operaciones
   