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

##############################   IMPLEMENT FACADE PATTERN   ##############################
class Facade:
    def __init__(self, componentes={}):
        self.gabinete = CabinetComposite() if  componentes.get('se agrega gabinete') else print('No se agrega gabinete')
        self.tarjetamadre = MotherboardComposite() if componentes.get('tarjeta madre') else print('No se agrega tarjeta madre')
        self.procesador = ProcessorLeaf() if componentes.get('procesador') else print('No se agrega procesador')
        self.grafica = GraphicsLeaf() if componentes.get('grafica') else print('No se agrega tarjeta grafica')
        self.memoria = MemoryLeaf() if componentes.get('memoria') else print('No se agrega memoria ')
        self.hdd = HDDLeaf() if componentes.get('hdd') else print ('No se agrega disco duro')
        self.nic = NICLeaf() if componentes.get('nic') else print ('No se agrega tarjeta de red')

def main():
    componentes= {
        'gabinete': True,
        'tarjeta madre': False,
        'procesador': True,
        'grafica': True,
        'memoria': False,
        'hdd': False,
        'nic': False
    }
    facade = Facade(componentes)
    

if __name__ == "__main__":
    main() 