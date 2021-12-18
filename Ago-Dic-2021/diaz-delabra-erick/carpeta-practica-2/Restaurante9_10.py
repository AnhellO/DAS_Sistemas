class Restaurant():
    def __init__(self, nombre, tipo):
        self.nombre = nombre.title()
        self.tipo = tipo

    def desc(self):
        print("\nEl mejor restaurant de todos! ---> " + self.nombre + " comida: " + self.tipo)
        
    def abierto(self):
        print("\n" + self.nombre + " esta abierto")
