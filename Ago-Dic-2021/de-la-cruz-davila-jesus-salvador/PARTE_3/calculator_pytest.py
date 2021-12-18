################################## PARTE 3 #################################
class Calculator:

    # Funcion que suma los numeros
    def suma(a, b) -> int:
        return a + b

    # Funcion que resta los numeros
    def resta(a, b) -> int:
        return a - b

    # Funcion que multiplica los numeros
    def multiplicacion(a, b) -> int:
        return a * b

    # Funcion que divide los numeros
    def division(a, b) -> float:
        if b == 0:
            return "No es posible dividir entre 0"
        else:
            return a / b

    # Funcion de eleva a una potencia
    def potencia(a, b) -> int:
        if b == 0:
            return 1
        else:
            return a ** b

    # Funcion para sacar raiz
    def raiz(a, b) -> float:
        if a < 0:
            return "No se puede raiz negativa"
        elif a == 0:
            return 0
        else:
            return pow(a, (1/(b)))