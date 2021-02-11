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
class SuiteFacade:
    def __init__(self, component={}):
        self.cabinet = CabinetComposite() if component.get("gabinete") else None
        self.mother = MotherboardComposite() if component.get("motherboard") else None
        self.processor = ProcessorLeaf() if component.get("procesador") else None
        self.grafica = GraphicsLeaf() if component.get("grafica") else None
        self.memoria = MemoryLeaf() if component.get("memoria") else None
        self.hdd = HDDLeaf() if component.get("hdd") else None
        self.nic = NICLeaf() if component.get("nic") else None
    
    def add_component(self):
        self.cabinet.spec if self.cabinet else print("No hay gabinete")
        self.mother.spec if self.mother else print("No hay motherboard")
        self.processor.spec if self.processor else print("No hay procesador")
        self.grafica.spec if self.grafica else print("No hay grafica")
        self.memoria.spec if self.memoria else print("No hay memoria")
        self.hdd.spec if self.hdd else print("No hay hdd")
        self.nic.spec if self.nic else print("No hay nic")
    
def main():
    component_suites = {
        'gabinete': True,
        'motherboard': True,
        'procesador': True,
        'grafica': True,
        'memoria': True,
        'hdd': True,
        'nic': True
    }
    xd = ProcessorLeaf()
    print(xd)
    Facade = SuiteFacade(component_suites)
    Facade.add_component()

if __name__ == "__main__":
    main()