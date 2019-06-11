import abc

class ComponenteGrafico(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def renderizar(self):
        pass

    def __init__(self, *args, **kwargs):
        pass

class Hijo(ComponenteGrafico):

    def __init__(self, *args, **kwargs):
        ComponenteGrafico.__init__(self, *args, **kwargs)
        self.name = args[0]

    def renderizar(self):

        print("\t{}".format(self.name))

class Composite():

    def __init__(self, *args, **kwargs):  # constructor
        ComponenteGrafico.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.hijos = []

    def add_hijo(self, hijo):

        self.hijos.append(hijo)

    def delete_hijo(self, hijo):

        self.hijos.remove(hijo)

    def renderizar(self):

        print("{}".format(self.name))


        for i in self.hijos:
            i.renderizar()

def main():

    ventana = Composite('---Ventana---')

    imagen = Composite('--Imagen--')
    panel = Composite('--Panel--')
    boton = Composite('--Botón--')
    etiqueta = Composite('-Etiqueta-')
    etiqueta1 = Composite('-Etiqueta-')
    input = Composite('-input-')

    ima = Hijo('imagen.jpg')
    texto = Hijo('Log-in to your account')
    texto1 = Hijo('Login')

    ventana.add_hijo(imagen)
    ventana.add_hijo(etiqueta)
    ventana.add_hijo(panel)

    imagen.add_hijo(ima)

    etiqueta.add_hijo(texto)
    etiqueta1.add_hijo(texto1)

    panel.add_hijo(input)
    panel.add_hijo(input)
    panel.add_hijo(boton)

    boton.add_hijo(etiqueta1)

    ventana.renderizar()

if __name__ == "__main__":
    main()
