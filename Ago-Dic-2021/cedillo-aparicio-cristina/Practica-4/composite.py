class componentElement:
    def details(self):
        pass

class LeafElement:
    def __init__(self, *args):
        # Toma el primer argumento posicional y lo asigna a la variable miembro posición
        self.posicion = args[0]

    def details(self):  # Devuelve la posición del elemento hijo
        # print("\t", end ="")
        return self.posicion

class CompositeElement:
    def __init__(self, *args):
        self.posicion = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def details(self):
        for child in self.children:
            if isinstance(child, LeafElement):
                print(f"'{self.posicion}' es supervisor de '{child.details()}'")
            else:
                print(f"'{self.posicion}' es superior de '{child.posicion}'")
                child.details()

