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
class Computadora():

    def __init__(self, usuario = "usuario"):
        self.is_on = False
        self.usuario = usuario

        self.gabinete = CabinetComposite()
        self.motherboard = MotherboardComposite()
        self.componentes = [ProcessorLeaf(), GraphicsLeaf(), MemoryLeaf(), HDDLeaf(), NICLeaf(),""]

        for componente in self.componentes:
            self.motherboard.add(componente)

        self.gabinete.add(self.motherboard)

    def display(self):
        with open("computadora.txt") as reader:
            content = reader.read().replace("[USER]", f"[{self.usuario.upper()}]")
            print(content)

    def toggle_on(self):
        if not self.is_on:
            print("Encendiendo computadora")
            sleep(1.2)
            self.display()
        else:
            print("Apagando computadora")
            sleep(1)

        self.is_on = not self.is_on

    def spec(self):
        if self.is_on:
            return self.gabinete.spec()

        return "Primero enciende la computadora..."


########
if __name__ == "__main__":
    
    my_computer = Computadora("anhello")

    ##### No se pueden hacer cosas si la computadora esta apagada
    print(my_computer.spec())

    ###### Prender computadora
    my_computer.toggle_on()

    ####### Specs de la computadora que armamos con el composite
    print(my_computer.spec())

    ###### Apagar computadora
    my_computer.toggle_on()

    ##### No se pueden hacer cosas si la computadora esta apagada
    print(my_computer.spec())

    ## Esto es un facade, por que a pesar de que tenemos nuestro objeto computadora, podemos seguir accesando
    ## funcionalidades de los componentes por si solos
    # print(my_computer.componentes[0].spec())
