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
    
    def divicion(self) -> int:
        if self.b > 0:
            return self.a / self.b
        else:
            return -99 #el -99 para definir numero indeterminado
            

    def potencia(self):
        return self.a ** self.b


    def raiz(self):
        if self.a < 0:
            cube_root = -99
        else:
            if self.b > 0:
                cube_root = pow(self.a,1/self.b)
            else:
                cube_root = -99 #el -99 para definir numero indeterminado
        return cube_root


#if x < 0:
        #x = abs(x)
        #cube_root = x**(1/3)*(-1)