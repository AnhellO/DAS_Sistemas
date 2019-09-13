from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def renderizar(self):
        pass

    def __init__(self, *args, **kwargs):
        pass

class Hijo(Componente):
    def __init__(self, *args, **kwargs):
        Componente.__init__(self, *args, **kwargs)
        self.name = args[0]

    def renderizar(self):
        print("\t{}".format(self.name))

class Composite():
    def __init__(self, *args, **kwargs):
        Componente.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.hijos = []

    def add_hijo(self, hijo):
        self.hijos.append(hijo)

    def delete_hijo(self, hijo):
        self.hijos.remove(hijo)

    def renderizar(self):
        print("{}".format(self.name))
        for hijo in self.hijos:
            hijo.renderizar()

def main():
    ventana = Composite('---Una Ventana---')
    # Hijos de ventana
    imagen = Composite('--Una Imagen--')
    panel = Composite('--Un Panel--')
    etiqueta1 = Composite('--Una Etiqueta--')
    etiqueta2 = Composite('--Otra Etiqueta--')
    # Agregar hijos a 'ventana'
    ventana.add_hijo(imagen)
    ventana.add_hijo(etiqueta1)
    ventana.add_hijo(panel)
    # Hijo de 'imagen'
    image = Hijo('imagen.jpg')
    # Agregar hijo a 'imagen'
    imagen.add_hijo(image)
    # Hijo de 'etiqueta1'
    texto1 = Hijo('Log-in to your account')
    # Agregar hijo a 'etiqueta1'
    etiqueta1.add_hijo(texto1)
    # Hijo de 'etiqueta2'
    texto2 = Hijo('Login')
    # Agregar hijo a 'etiqueta2'
    etiqueta2.add_hijo(texto2)
    # Hijos de panel
    input1 = Composite('--Un Input--')
    input2 = Composite('--Otro Input--')
    boton = Composite('--Un Botón--')
    # Agregar hijos a 'panel'
    panel.add_hijo(input1)
    panel.add_hijo(input2)
    panel.add_hijo(boton)
    # Hijo de 'boton'
    texto = Hijo('--Texto del Boton--')
    # Agregar hijo a 'boton'
    boton.add_hijo(texto)
    # A renderizar 'ventana' para mostrarla
    ventana.renderizar()

if __name__ == "__main__":
    main()
