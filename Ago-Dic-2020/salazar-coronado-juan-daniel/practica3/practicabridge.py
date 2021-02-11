from abc import ABC, abstractmethod

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

class Implementor(ABC):
    @abstractmethod
    def operation_imp(self, a, b):
        pass

class ImplementorSuma(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a + b
        return "Suma de {} y {} = {}".format(a, b, self.resultado)
        
class ImplementorResta(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a - b
        return "Resta de {} y {} = {}".format(a, b, self.resultado)

class ImplementorDivision(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a / b
        return "División de {} y {} = {}".format(a, b, self.resultado)

class ImplementorMultiplicacion(Implementor):
    def operation_imp(self, a, b):
        self.resultado = a * b
        return "Multiplicación de {} y {} = {}".format(a, b, self.resultado)


def main():
    unasuma = ImplementorSuma()
    abstraction = Abstraction(unasuma)
    abstraction.operation(float(5), float(4))

    abstractionext = ExtendedAbstraction(unasuma)
    abstractionext.operation(float(6), float(7))

    #unaresta = ImplementorResta()
    #abstraction2 = Abstraction(unaresta)
    #abstraction2.operation(float(5), float(4))

    #unamultiplicacion = ImplementorMultiplicacion()
    #abstraction3 = Abstraction(unamultiplicacion)
    #abstraction3.operation(float(5), float(4))

    #unadivision = ImplmentorDivision()
    #abstraction4 = Abstraction(unadivision)
    #abstraction4.operation(float(5), float(4))

if __name__ == "__main__":
    main()