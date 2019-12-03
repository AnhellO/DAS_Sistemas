class Personas(object):
    def __init__(self, nombre, edad, genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero

    def set_nombre(self, nombre):
        self.nombre= nombre
    def set_edad(self, edad):
        self.edad= edad
    def set_genero(self, genero):
        self.genero=genero
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_genero(self):
        return self.genero
    def __str__(self):
        return 'Nombre: {}\nEdad: {}\n Genero: {}'.format(self.nombre, self.edad, self.genero).strip()