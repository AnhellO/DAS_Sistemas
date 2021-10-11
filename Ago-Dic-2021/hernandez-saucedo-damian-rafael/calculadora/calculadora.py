class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b
    
    def multi(self) -> int:
        return self.a * self.b
    
    def divicion(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "indeterminado" 
            

    def potencia(self):
        return self.a ** self.b


    def raiz(self):
        if self.a < 0:
            cube_root = "indeterminado"
        else:
            if self.b > 0:
                cube_root = pow(self.a,1/self.b)
            else:
                cube_root = "indeterminado" 
        return cube_root


