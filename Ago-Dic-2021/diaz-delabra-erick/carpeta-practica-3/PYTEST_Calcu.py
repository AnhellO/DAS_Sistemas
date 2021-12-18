
'''PARTE 3 OPCIONAL: PYTEST'''

class Calculator:   
    def suma(a, b) -> int:
        return a + b
    
    def resta(a, b) -> int:
        return a - b

    def multiplicacion(a, b) -> int:
        return a * b

    def division(a, b) -> int:
        if b == 0:
            return "No se puede dividir entre 0"
        else:
            return (a / b)

    def raizNumero(a, b) -> int:
        if a < 0:
            return "No se puede raiz de negativos"
        else:
            return pow(a, (1/(b)))

    def potencia(a, b) -> int:
        return pow(a, b)