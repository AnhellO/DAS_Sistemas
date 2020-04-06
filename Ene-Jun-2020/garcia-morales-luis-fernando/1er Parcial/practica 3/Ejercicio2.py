import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass
    
class ArchivoComposite(ArchivoComponent):
    def __init__(self):
        self.child_directory = []
    
    def add(self, component):
        self.child_directory.append(ArchivoLeaf.union)

    def remove(self, component):
        self.child_directory.remove(ArchivoLeaf.union)
    
    def imprimeEstructura(self):
        for child in self.child_directory:
            print(child)

class ArchivoLeaf(ArchivoComposite):
    def __init__(self):
        self.nombre = None
        self.tipo = None
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_tipo(self, tipo):
        self.tipo = tipo
    def union(self):
        print(self.nombre+self.tipo)
    def imprimeEstructura(self):
        pass
def main():
    leaf = ArchivoLeaf()
    directorio = ArchivoComposite()
    leaf.set_nombre("documento")
    leaf.set_tipo("doc")
    directorio.add(leaf)
    directorio.imprimeEstructura
if __name__ == "__main__":
    main()