import abc

# Component
class ComponenteGrafico(metaclass=abc.ABCMeta):
    #Generalmente es una interface o clase abstracta la cual tiene las operaciones mínimas que serán
    #utilizadas, este componente deberá ser extendido por los otros dos componentes Leaf y Composite.

    @abc.abstractmethod
    def renderizar(self):
        pass

    def _init_(self, *args, **kwargs):
        pass

# Leaf
class Leaf(ComponenteGrafico):
    #El leaf u hoja representa la parte más simple o pequeña de toda la estructura y este extiende
    #o hereda de Component.
    def _init_(self, *args, **kwargs):
        ComponenteGrafico._init_(self, *args, **kwargs)
        self.name = args[0]

    def renderizar(self):
        print("\t{}".format(self.name))

# Composite
class Composite(ComponenteGrafico):
    #Este componente es por lo general un Interface o Clase abstracta  por lo que podremos agregamos objetos
    #de tipo Composite o Leaf.
    def _init_(self, *args, **kwargs):
        ComponenteGrafico._init_(self, *args, **kwargs)
        self.name = args[0]
        self.hijos = []

    def add_hijo(self, hijo):
        self.hijos.append(hijo)

    def delete_hijo(self, hijo):
        self.hijos.remove(hijo)

    def renderizar(self):
        print("{}".format(self.name))

        # Itera através de los objetos child e invoca la función componente imprimiendo sus nombres
        for i in self.hijos:
            i.renderizar()

def main():
    # Nodo raíz
    ventana = Composite('*Ventana')

    # Nodos padres
    imagen = Composite('*Imagen')
    panel = Composite('*Panel')
    boton = Composite('*Botón')
    etiqueta = Composite('*Etiqueta')
    input = Composite('*Input')


    ima = Leaf('*imagen.jpg')
    texto = Leaf('*Log-in to your account')
    texto1 = Leaf('*Login')

    ventana.add_hijo(imagen)
    ventana.add_hijo(etiqueta)
    ventana.add_hijo(panel)

    imagen.add_hijo(ima)

    etiqueta.add_hijo(texto)

    panel.add_hijo(input)
    panel.add_hijo(input)
    panel.add_hijo(boton)

    boton.add_hijo(texto1)

    ventana.renderizar()

if __name__ == "_main_":
    main()