from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Componente
class ArchivoComponent(ABC):
    @property
    def parent(self) -> ArchivoComponent:
        return self._parent
    
    @parent.setter
    def parent (self, parent: ArchivoComponent):
        self._parent = parent
    @abstractmethod
    def imprimeEstructura(self):
        pass

    # Nombre del archivo
    def get_nombre(self):
        return self.nombre

    # Directorio o archivo
    def get_tipo(self):
        return self.tipo

    def add(self, archivo: ArchivoComponent) -> None:
        pass

    def is_composite(self) -> bool:
        return False


class leaf(ArchivoComponent):
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.tipo = "Archivo"

    def imprimeEstructura(self) -> str:
        return f"/{self.get_tipo()}:{self.get_nombre()}"

class Composite(ArchivoComponent):
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.tipo = "Directorio"
        self._children: List[ArchivoComponent] = []

    def add(self, archivo: ArchivoComponent) -> None:
        self._children.append(archivo)
        archivo.parent = self

    def is_composite(self) -> bool:
        return True

    def imprimeEstructura(self):
        results = []
        for child in self._children:
            results.append(child.imprimeEstructura())
        return f"/{self.get_tipo()}{''.join(results)}"

def client_code(archivo: ArchivoComponent) -> None:
    print(f"Result: {archivo.imprimeEstructura()}", end ="")

def client_code2(archivo1: ArchivoComponent, archivo2: ArchivoComponent) ->None:
    if archivo1.is_composite():
        archivo1.add(archivo2)

    print(f"Result: {archivo1.imprimeEstructura()}", end="")
