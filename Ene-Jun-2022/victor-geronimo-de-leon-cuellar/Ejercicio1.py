import abc
from ctypes import addressof

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

    def Nuevo(self, Archivo: ArchivoComponent) -> None:
        pass     

class compruebastr(ArchivoComponent):
    def comprueba (self)->str:
     return"Leaf"

   
import unittest
class LeafTest(unittest.TestCase):
    Nuevo = addressof.__new__('Pascal')
    compruebastr.get_nombre('Pascal')
    self.asserEqual(leaf.get_nombre,'Pascal')

        print(ArchivoComponent.comprueba()}, end="")
