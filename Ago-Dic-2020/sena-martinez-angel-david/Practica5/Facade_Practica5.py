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
        return f"{4*' '}Procesador: Intel Core I7 "

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


##########IMPLEMENTO FACADE###############


class Computadora():

    def __init__(self, user):
        self.on = False
        self._user = user
        self.gabinete = CabinetComposite()
        self.motherboard = MotherboardComposite()
        self.componentes = [ProcessorLeaf(), GraphicsLeaf(), MemoryLeaf(), HDDLeaf(), NICLeaf()]

        for i in self.componentes:
            self.motherboard.add(i)

        self.gabinete.add(self.motherboard)

    def encender(self):
        if (self.on == False):
            print("Encendiendo computadora")
            sleep(1)
            self.on = True

    def apagar(self):
        if (self.on == True):
            print("Apagando Computadora")
            sleep(2)
            self.on = False


    def pantalla(self,cambiar):
       if (cambiar == True):
            self.apagar()

    def especificaciones(self):
        if (self.on == True):
            return f"La Computadora de {self._user} tiene las siguientes especificaciones:\n{ self.gabinete.spec()}"
        return "La computadora esta apagada"


def main():
    mi_compu = Computadora("DavidSena87")

    ### Prender computadora
    mi_compu.encender()

    ### Muestra la Pantalla
    cambio = False
    question = input("Desea apagar la computadora?  True or False\n")
    if (question == "True"):
        cambio = True
    if (question == "False"):
        cambio = False
    mi_compu.pantalla(cambio)


    ### Specs de la computadora que armamos con el composite
    specs = mi_compu.especificaciones()
    print(specs)

if __name__ == "__main__":
    main() 