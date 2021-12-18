from math import pow
class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b
    #parte 1 y 2
    def multiplicacion(self) ->int:
        return self.a * self.b
    
    def division(self) ->float:
        if self.b!=0:
            return self.a / self.b
        else:
            return "Favor de hacer una operación valida, MATH ERROR"
    
    def potencia(self) ->int:
        return self.a ** self.b

    def raiz(self) ->float:     #'B' es mi base y 'A' mi numero a sacar raiz
        if self.b%2==0 and self.a<0:        #Caso para una raiz par y la raiz de un numero negativa
            return "Error!!!"
        elif self.b%2!=0 and self.a<0:      #Caso para una raiz no par(cubica etc.) y la raiz de un numero negativa
            return -pow(abs(self.a),(float(1)/self.b))
        else:       #caso para una raiz de un numero positiva
            return pow(self.a,(float(1)/self.b))



