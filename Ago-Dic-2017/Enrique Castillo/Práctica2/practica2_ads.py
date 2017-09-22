import abc

class comprar_pizza(metaclass=abc.ABCMeta):
    #Template method
    def pedir_pizza(self):
        self.eleir_masa()
        self.pedir_ingredientes()
        self.pagar()

    @abc.abstractmethod
    def elegir_masa(self):
        pass
    @abc.abstractmethod
    def pedir_ingredientes(self):
        pass
    @abc.abstractmethod
    def pagar(self):
        pass

class pedir_por_tel(comprar_pizza):
    def hablar_restaurant(self):
        pass

    def elegir_masa(self):
        print("masa de sarten")

    def pedir_ingredientes(self):
        print("solo piña")

    def pagar(self):
        print("mi orden es gratis")

class ir_por_ella(comprar_pizza):
    def ir_restaurant(self):
        pass

    def elegir_masa(self):
        print("masa de sarten")

    def pedir_ingredientes(self):
        print("solo piña")

    def pagar(self):
        print("no traigo dinero")

def main():
    pizza1 = pedir_por_tel()
    pizza1.pedir_pizza()

    pizza2 = ir_por_ella()
    pizza2.pedir_pizza()

if __name__ == "__main__":
    main()    
