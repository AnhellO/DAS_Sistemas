#Goncho
from abc import ABCMeta, abstractstaticmethod

class CajeroHandler(metaclass = ABCMeta):
    """" manejar solicitudes """

    @abstractstaticmethod
    def set_successor(successor):
        """ Establecer el siguiente controlador en la cadena """

    @abstractstaticmethod
    def handle(cantidad):
        """ Manejar el evento """    
    
class Dispensador50(CajeroHandler):
    """ Dispensador de $50 
        si corresponde; de ​​lo contrario, 
        continúe con el siguiente 
    """

    def __init__(self):
        self.siguiente = None

    def set_successor(self, siguiente):
        self.siguiente = siguiente

    def handle(self, cantidad):
        if cantidad >= 50:
            num = cantidad // 50
            residuo = cantidad % 50
            print(f"Repartiendo {num} Billete de $50")
            if residuo != 0:
                self.siguiente.handle(residuo)
        else:
            self.siguiente.handle(cantidad)

class Dispensador20(CajeroHandler):
    """ Dispensador de $20 
        si corresponde; de ​​lo contrario, 
        continúe con el siguiente 
    """
    def __init__(self):
        self.siguiente = None

    def set_successor(self, siguiente):
        self.siguiente = siguiente

    def handle(self, cantidad):
        if cantidad >= 20:
            num = cantidad // 20
            residuo = cantidad % 20
            print(f"Repartiendo {num} Billete de $20")
            if residuo != 0:
                self.siguiente.handle(residuo)
        else:
            self.siguiente.handle(cantidad)
    
class Dispensador10(CajeroHandler):
    """ Dispensador de $10 
        si corresponde; de ​​lo contrario, 
        continúe con el siguiente 
    """
    def __init__(self):
        self.siguiente = None

    def set_successor(self, siguiente):
        self.siguiente = siguiente

    def handle(self, cantidad):
        if cantidad >= 10:
            num = cantidad // 10
            residuo = cantidad % 10
            print(f"Repartiendo {num} Billete de $10")
            if residuo != 0:
                self.siguiente.handle(residuo)
        else:
            self.siguiente.handle(cantidad)

class dispensador_chain:

    def __init__(self):
        #Inicializamos el sigiente chain
        self.chain1 = Dispensador50()
        self.chain2 = Dispensador20()
        self.chain3 = Dispensador10()

        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)

def main():
    """ Solicitamos la cantidad a retirar y 
        prosegimos a dar los diferentes
        tipos de villetes
    """
    ATM = dispensador_chain()
    Cantidad = int(input("Ingrese cantidad a retirar en multiplo de 10: "))
    ATM.chain1.handle(Cantidad)


if __name__ == "__main__":
     main()           
                
