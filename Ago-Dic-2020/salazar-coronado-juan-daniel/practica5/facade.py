import abc

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

class SuitesFacade:
    def __init__(self, componentes={}):
        self.gabinete = CabinetComposite() if componentes.get('gabinete') else None
        self.motherboard = MotherboardComposite() if componentes.get('motherboard') else None
        self.processor = ProcessorLeaf() if componentes.get('processor') else None
        self.graphics = GraphicsLeaf() if componentes.get('graphics') else None
        self.memory = MemoryLeaf() if componentes.get('memory') else None
        self.hdd = HDDLeaf() if componentes.get('hdd') else None
        self.nic = NICLeaf() if componentes.get('nic') else None

    def agregar_componentes(self):
        self.gabinete if self.gabinete else print('No se agrega gabinete')
        self.motherboard if self.motherboard else print('No se agrega motherboard')
        self.processor.spec() if self.processor else print('No se agregan procesadores')
        self.graphics.spec() if self.graphics else print('No se agrega tarjeta grafica')
        self.memory.spec() if self.memory else print('No se agrega memoria ram')
        self.hdd.spec() if self.hdd else print ('No se agrega disco duro')
        self.nic.spec() if self.nic else print ('No se agrega tarjeta de red')

def main():
    componentes_suites = {
        'gabinete': True,
        'motherboard': True,
        'processor': True,
        'graphics': True,
        'memory': True,
        'hdd': True,
        'nic': True
    }

    facade = SuitesFacade(componentes_suites)
    facade.agregar_componentes()

if __name__ == "__main__":
    main()