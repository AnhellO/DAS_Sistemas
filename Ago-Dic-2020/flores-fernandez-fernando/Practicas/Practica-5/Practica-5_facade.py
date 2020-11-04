import abc
from time import sleep

#################################################################################################
#										COMPOSITE												#
#################################################################################################

class ComputerComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def spec(self):
        pass

class BaseComposite(ComputerComponent):
    def __init__(self):
        self._child_components = []

    def spec(self):
        structure = []
        for child in self._child_components:
            if isinstance(child, str):
                structure.append(child)
                continue

            structure.append(child.spec())

        return '\n'.join(structure)

    def add(self, component: ComputerComponent):
        self._child_components.append(component)
        return self

    def remove(self, component: ComputerComponent):
        self._child_components.remove(component)
        return self

class CabinetComposite(BaseComposite):
    def __init__(self):
        self._child_components = ["\nGabinete: Asus ROG"]

class MotherboardComposite(BaseComposite):
    def __init__(self):
        self._child_components = [f"{2*' '}Tarjeta Madre: Gigabyte B450M"]

class ProcessorLeaf(ComputerComponent):
    def spec(self):
        return f"{4*' '}Procesador: AMD Ryzen 5 3600"

class GraphicsLeaf(ComputerComponent):
    def spec(self):
        return f"{4*' '}Tarjeta Gráfica: Nvidia Geforce RTX 3070"

class MemoryLeaf(ComputerComponent):
    def spec(self):
        return f"{4*' '}Memoria RAM: Hyper X"

class HDDLeaf(ComputerComponent):
    def spec(self):
        return f"{4*' '}Disco Duro: SSD Kingston 960TB"

class NICLeaf(ComputerComponent):
    def spec(self):
        return f"{4*' '}Tarjeta de Red: AX WIFI 6"


#################################################################################################
#										FACADE													#
#################################################################################################


class Pc():

    def __init__(self, usuario):
        self.on = False
        self._usuario = usuario
        self.gabinete = CabinetComposite()
        self.motherboard = MotherboardComposite()
        self.componentes = [ProcessorLeaf(), GraphicsLeaf(), MemoryLeaf(), HDDLeaf(), NICLeaf()]

        for i in self.componentes:
            self.motherboard.add(i)

        self.gabinete.add(self.motherboard)

    def encender(self):
        if (self.on == False):
            print("Encendiendo computadora")
            sleep(2)
            self.on = True
    
    def apagar(self):
        if (self.on == True):
            print("Apagando Computadora")
            sleep(4)
            self.on = False


    def pantalla(self,cambiar):
       if (cambiar == True):
            self.apagar()

    def specs(self):
        if (self.on == True):
            return f"La Computadora de {self._usuario} Tiene los siguientes Specs:\n{self.gabinete.spec()}"
        return "La computadora no esta encendida"


def main():
    my_Pc = Pc("Rephyroth")

    ### Prender computadora
    my_Pc.encender()

    ### Muestra la Pantalla
    cambio = False
    des = input("Desea apagar la computadora?, True or False\n")
    if (des == "True"):
        cambio = True
    if (des == "False"):
        cambio = False
    my_Pc.pantalla(cambio)


    ### Specs de la computadora que armamos con el composite
    specs = my_Pc.specs() 
    print(specs)

if __name__ == "__main__":
    main()