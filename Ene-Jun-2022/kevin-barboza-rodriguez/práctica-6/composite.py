import abc

# Componente
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        print(f'{self.get_tipo()}/{self.get_nombre()}')

    # Nombre del archivo
    def get_nombre(self):
        return self.nombre

    # Directorio o archivo
    def get_tipo(self):
        return self.tipo

#Elemento
class ElementoLeaf(ArchivoComponent):
    # nombre, tipo

    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def imprimeEstructura(self):
        super().imprimeEstructura()

#contenedor
class ArchivoComposite(ArchivoComponent):
    
    def __init__(self):
        self.component = []

    def imprimeEstructura(self):
         super().imprimeEstructura()

    def add(self,hoja):
        self.component.append(hoja)  

    def remove(self,hoja):
        self.component.remove(hoja)

    def get_children(self,hoja):
        for i in range(len(self.component)):
            if self.component[i] == hoja:
                hoja.imprimeEstructura()
    

if __name__ == "__main__":

    contenedor = ArchivoComposite()

    hoja = ElementoLeaf('kevin', 'user')
    hoja.imprimeEstructura()
    print(hoja.get_nombre())
    hoja_1 = ElementoLeaf('raquel', 'user')
    hoja_2 = ElementoLeaf('edson', 'user')

    contenedor.add(hoja)
    contenedor.add(hoja_1)
    contenedor.add(hoja_2)
    contenedor.remove(hoja_1)

    contenedor.get_children(hoja)
