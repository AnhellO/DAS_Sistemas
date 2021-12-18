class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a+self.b
    
    def resta(self) -> int:
        return self.a-self.b
    
    def multi(self) -> int:
        return self.a*self.b
    
    def divi(self) -> int:
        if self.b == 0:
            return "Error: No es posible dividir entre cero"
        else:
            return self.a/self.b
    
    def pote(self) -> int:
        return self.a**self.b
    
    def raiz(self) -> int:
        if self.b < 0:
            return "Error: No es posible obtener raices de numeros negativos"
        else:
            return self.b**(1/self.a)