  
class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b
    
    def Multiplicion(self)-> int:
        return self.a * self.b
    
    def Division(self)-> float:
        if self.b == 0:
            return "indefinido"
        else:
            return self.a/self.b
    
    def potencia(self):
        return pow(self.a,self.b)
    
    
    def raiz (self)->float:
        if (self.b)!=0:
            if  (self.b%2)== 0:
                if self.a > 0:
                    return pow(self.a, (1/self.b))
                else:
                    return "numero imaginario"
            else:
                if self.a > 0:
                    return pow(self.a, (1/self.b))
                else:
                    return -(pow(-self.a, (1/self.b)) )
        else:
            return "indefinido"

mi_calculadora =Calculator(4,-2)
print(mi_calculadora.raiz())