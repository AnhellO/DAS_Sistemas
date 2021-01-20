import abc
import time

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
        self._child_components = ["Gabinete: Asus ROG"]

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
 
  

class Computadora:
    def __init__(self, user):
        self.__encendida = False
        self.user = user
        self.__computadora = CabinetComposite().add(
            MotherboardComposite()
                .add(ProcessorLeaf())
                .add(GraphicsLeaf())
                .add(HDDLeaf())
                .add(MemoryLeaf())
                .add(NICLeaf())
        )

    def turn_on(self):
        if self.__encendida == False:
            print("The computer is turning on...")
            time.sleep(5)
            self.__encendida = True
            print(f"Welcome {self.user} ʘ‿ʘ!")
            show_specs = input("Do you wanna know your pc specifications? 's' si, cualquier otro valor para no: ")#usando el espanglish como dvd
            if (show_specs.lower() == 's'):
                print(self.__computadora.spec())
            

    def turn_off(self):
        if self.__encendida == True:
            print("Turning off the computer...")
            time.sleep(3)
            print(f"Bye bye {self.user} ಥ﹏ಥ")
            self.__encendida = False
        
if __name__ == "__main__": 
  
    compu = Computadora("Arnold-MSI")
    compu.turn_on()
    compu.turn_off()