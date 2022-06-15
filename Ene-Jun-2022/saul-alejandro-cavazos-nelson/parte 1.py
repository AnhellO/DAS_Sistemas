import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass

    # Nombre del archivo
    def get_nombre(self):
        return self.nombre

    # Directorio o archivo
    def get_tipo(self):
        return self.tipo
    
    def add(self, Archivo: ArchivoComponent) -> None:
        pass
    def remove(self, Archivo: ArchivoComponent) -> None:
        pass
    def is_composite(self) -> bool:
        return False

class Leaf(ArchivoComponent):
    def operation (self)->str:
     return"hoja"

class compositive (ArchivoComponent):
    def __init__(self) -> None:
        self._children: List[ArchivoComponent] = []
    def add(self, Archivo: ArchivoComponent) -> None:
        self._children.append[ArchivoComponent]
        ArchivoComponent.parent = self
    def remove(self, Archivo: ArchivoComponent) -> None:
        self._children.remove(ArchivoComponent)
        ArchivoComponent.parent = None
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
    def client_code(Archivo: ArchivoComponent)-> None:
        print(f"RESULT: {ArchivoComponent.operation()}", end="")
    def client_code2(Archivo1: ArchivoComponent,Archivo2: ArchivoComponent)-> None:
        if Archivo1.is_composite():
            Archivo1.add(Archivo2)

        print(f"RESULT: {ArchivoComponent.operation()}", end="")
    