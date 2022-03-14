import copy

class Oveja():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo


def main():
    original = Oveja('Dolly','Oveja de granja')
    clon1 = copy.copy(original)
    

    print(f"Original:\nNombre : {original.get_nombre()}\nTipo : {original.get_tipo()}\n")    

    print(f"Clon:\nNombre : {clon1.get_nombre()}\nTipo : {clon1.get_tipo()}\n")

    original.set_nombre('Dolores')
    print(f"Original:\nNombre : {original.get_nombre()}\nTipo : {original.get_tipo()}\n")

    print(f"Clon:\nNombre : {clon1.get_nombre()}\nTipo : {clon1.get_tipo()}\n")

    #print(original == clon1)


if __name__ == '__main__':
    main()
