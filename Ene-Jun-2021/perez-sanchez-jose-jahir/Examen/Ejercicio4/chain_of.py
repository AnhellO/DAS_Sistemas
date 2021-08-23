from abc import ABC, abstractmethod
#La interface handler
class CajeroHandler(ABC):
    @abstractmethod
    def next_succesor(self, handler):
        pass
    
    @abstractmethod
    def handle(self, request):
        pass
#La clase abstracta que tendra el metodo next_succesor para decidir el orden de la cadena y el metodo handler para pasar el request al siguiente concrete handler
class AbstractHandler(CajeroHandler):

    _next_handler: CajeroHandler = None

    def next_succesor(self,handler: CajeroHandler) -> CajeroHandler:
        self._next_handler = handler

        return handler
    
    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
#Cada concrete que el problema necesita, que obtiene el request, saca las veces que cabe en el por el numero que es, por ejemplo 50 % 50 da 1
#tambien obtiene cuantos billetes son y los impreme, al final pasa lo que sobra al siguiente handler
class Cajero10ConcreteHandler(AbstractHandler):
    def handle(self,request):
        resto = request % 10
        nbilletes = request / 10
        if (int(nbilletes)>0):
            print(f"{int(nbilletes)} x 10 $")
        if (resto>0):
            return super().handle(resto)

class Cajero20ConcreteHandler(AbstractHandler):
    def handle(self,request):
        resto = request % 20
        nbilletes = request / 20
        if (int(nbilletes)>0):
            print(f"{int(nbilletes)} x 20 $")
        if (resto>0):
            return super().handle(resto)

class Cajero50ConcreteHandler(AbstractHandler):
    def handle(self,request):
        resto = request % 50
        nbilletes = request / 50
        if (nbilletes>0):
            print(f"{int(nbilletes)} x 50 $")
        if (resto>0):
            return super().handle(resto)

#El metodo main para hacer las pruebas que necesite
def main():
    b50 = Cajero50ConcreteHandler()
    b20 = Cajero20ConcreteHandler()
    b10 = Cajero10ConcreteHandler()

    b50.next_succesor(b20).next_succesor(b10)

    print("Dinero que desea retirar:")
    sum = int(input())
    b50.handle(sum)

if __name__ == "__main__":
    main()