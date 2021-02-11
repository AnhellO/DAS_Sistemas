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
class computer_facade():
    estatus_activo = False
       
    
    def __init__(self,pc_name:str):
        self.name = pc_name
        self.estatus_activo = False
        self.cabinet = CabinetComposite()
        motherb = MotherboardComposite()
        processor = ProcessorLeaf()
        gpu = GraphicsLeaf()
        ram = MemoryLeaf()
        storage = HDDLeaf()
        nic = NICLeaf()

        motherb.add(processor)
        motherb.add(gpu)
        motherb.add(ram)
        motherb.add(storage)
        motherb.add(nic)
        self.cabinet.add(motherb)

    def pulsar_boton_de_encendido(self,_seconds:int):
        if self.estatus_activo == True and _seconds < 10:
            print("La pc ya se encuentra encendida")
            
        elif self.estatus_activo == True and _seconds >= 10:
            self.estatus_activo = False
            print("La pc se ha apagado")

        elif self.estatus_activo == False: 
            self.estatus_activo = True
            print("La pc se esta encendiendo...")
            time.sleep(5)
            print("La pc ahora esta encendida")


    def print_especificaciones(self):
        if self.estatus_activo == True:
            print(self.name)
            print(self.cabinet.spec())

    def display_some_work(self):
        if self.estatus_activo == True:
            print(f"Actualmente estas haciendo cosas muy importantes en tu PC")
       


def main():

    compu = computer_facade("John-Desktop-Ubuntu")
    compu.pulsar_boton_de_encendido(1)
    compu.print_especificaciones()
    compu.display_some_work()
    compu.pulsar_boton_de_encendido(10)



if __name__ == "__main__":
    main()