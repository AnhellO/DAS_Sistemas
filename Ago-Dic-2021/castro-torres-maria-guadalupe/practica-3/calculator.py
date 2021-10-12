import math 

class Calculator:
    
    def suma(a, b) -> int:
        return a + b
    
    def resta(a, b) -> int:
        return a - b

    def multiplicacion(a, b)->int:
        return a * b 

    def division(a, b)->int:
        if b == 0:
            return "El divisor no puede ser cero"
        else:
          return a / b    


    def potencia(a, b)->int:
        return pow(a , b )

    def raiz(a, b)->int:
        if a < 0:
            return "No se puede calcular la raiz de numeros negativos"
        else:    
         return (b * (math.sqrt(a)))       