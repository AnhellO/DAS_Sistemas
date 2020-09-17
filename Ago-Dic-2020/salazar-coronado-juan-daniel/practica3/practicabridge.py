
class Abstraction:
    def __init__(self, imp):
        self._imp = imp

    def operation(self, a, b):
        self._a = a
        self._b = b
        print("Haciendo uso de la abstracción normal\n"
                f"{self._imp.operation_imp(self._a, self._b)}")

class ExtendedAbstraction(Abstraction):
    def operation(self, a, b):
        self._a = a
        self._b = b
        print("Haciendo uso de la abstracción extendida\n"
                f"{self._imp.operation_imp(self._a, self._b)}")

class Implementor():
    def operation_imp(self, a, b):
        pass

class suma(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a + b
        return "Suma de {} y {} = {}".format(a, b, self.resultado)
        
class resta(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a - b
        return "Resta de {} y {} = {}".format(a, b, self.resultado)

class division(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a / b
        return "División de {} y {} = {}".format(a, b, self.resultado)

class multiplicacion(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a * b
        return "Multiplicación de {} y {} = {}".format(a, b, self.resultado)


def main():
    unasuma = suma()
    abstraction = Abstraction(unasuma)
    abstraction.operation(float(5), float(4))

    abstractionext = ExtendedAbstraction(unasuma)
    abstractionext.operation(float(6), float(7))

    #unaresta = resta()
    #abstraction2 = Abstraction(unaresta)
    #abstraction2.operation(float(5), float(4))

    #unamultiplicacion = multiplicacion()
    #abstraction3 = Abstraction(unamultiplicacion)
    #abstraction3.operation(float(5), float(4))

    #unadivision = division()
    #abstraction4 = Abstraction(unadivision)
    #abstraction4.operation(float(5), float(4))

if __name__ == "__main__":
    main()