from abc import ABC, abstractmethod

class ComponenteGrafico(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class ComponenteGraficoLeaf(ComponenteGrafico):
    def __init__(self, *args, **kwargs):
        self.name = args[0]

    def renderizar(self):
        return self.name

class ComponenteGraficoComposite(ComponenteGrafico):
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.hijos = []

    def add_hijo(self, hijo):
        self.hijos.append(hijo)

    def delete_hijo(self, hijo):
        self.hijos.remove(hijo)

    def renderizar(self):
        for hijo in self.hijos:
            if isinstance(hijo, ComponenteGraficoLeaf):
                print(f"Componente '{self.name}': '{hijo.renderizar()}'")
            else:
                print(f"Componente '{self.name}' contiene '{hijo.name}'")
                hijo.renderizar()

def main():
    ventana = ComponenteGraficoComposite('Ventana')
    # Hijos de ventana
    imagen = ComponenteGraficoComposite('Imagen')
    panel = ComponenteGraficoComposite('Panel 1')
    etiqueta1 = ComponenteGraficoComposite('Etiqueta 1')
    panel2 = ComponenteGraficoComposite('Panel 2')
    # Agregar hijos a 'ventana'
    ventana.add_hijo(imagen)
    ventana.add_hijo(etiqueta1)
    ventana.add_hijo(panel)
    ventana.add_hijo(panel2)
    # Hijo de 'imagen'
    image = ComponenteGraficoLeaf('imagen.jpg')
    # Agregar hijo a 'imagen'
    imagen.add_hijo(image)
    # Hijo de 'etiqueta1'
    texto1 = ComponenteGraficoLeaf('Log-in to your account')
    # Agregar hijo a 'etiqueta1'
    etiqueta1.add_hijo(texto1)
    # Hijos de panel
    input1 = ComponenteGraficoComposite('Input')
    input2 = ComponenteGraficoComposite('Input')
    boton = ComponenteGraficoComposite('Botón')
    # Agregar hijos a 'panel'
    panel.add_hijo(input1)
    panel.add_hijo(input2)
    panel.add_hijo(boton)
    # Hijos de 'boton'
    etiqueta2 = ComponenteGraficoComposite('Etiqueta 2')
    texto2 = ComponenteGraficoLeaf('Login')
    # Agregar hijos a 'boton'
    etiqueta2.add_hijo(texto2)
    boton.add_hijo(etiqueta2)
    # Hijos de 'panel 2'
    etiqueta3 = ComponenteGraficoComposite('Etiqueta 3')
    texto3 = ComponenteGraficoLeaf('New to us? Sign Up')
    etiqueta3.add_hijo(texto3)
    panel2.add_hijo(etiqueta3)
    # A renderizar 'ventana' para mostrarla
    ventana.renderizar()

if __name__ == "__main__":
    main()
