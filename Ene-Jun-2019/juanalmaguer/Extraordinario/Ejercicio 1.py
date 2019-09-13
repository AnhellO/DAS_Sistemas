import abc

class ComponenteGrafico(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def renderizar(self):
        pass

    def _init_(self, *args, **kwargs):
        pass

class Hijo(ComponenteGrafico):
    #Hereda de la clase abstracta ComponenteGrafico

    def _init_(self, *args, **kwargs):
        ComponenteGrafico._init_(self, *args, **kwargs)
        self.name = args[0]

    def renderizar(self):
        print("\t{}".format(self.name))

class Composite():
    #Hereda de la clase abstracta

    def _init_(self, *args, **kwargs):#Constructor
        ComponenteGrafico._init_(self, *args, **kwargs)
        self.name = args[0]  # aquí guardamos el nombre de nuestro objeto composite
        self.hijos = []  # aquí guardamos nuestros hijos

    def add_hijo(self, hijo):
        #Método para agregar un nuevo hijo
        self.hijos.append(hijo)

    def delete_hijo(self, hijo):
        #Elimina un hijo
        self.hijos.remove(hijo)

    def renderizar(self):
        #Imprime el nombre del composite
        print("{}".format(self.name))

        # Itera através de los objetos child e invoca la función componente imprimiendo sus nombres
        for i in self.hijos:
            i.renderizar()

def main():
    # Nodo raíz
    ventana = Composite('Ventana')

    # Nodos padres
    imagen = Composite('Imagen')
    panel = Composite('Panel')
    boton = Composite('Botón')
    etiqueta = Composite('Etiqueta')
    input = Composite('input')

    # Ramificaciones
    ima = Hijo('imagen.jpg')
    texto = Hijo('Log-in to your account')
    texto1 = Hijo('Login')

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