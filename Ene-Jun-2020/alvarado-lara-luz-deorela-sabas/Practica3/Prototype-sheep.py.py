import copy
class Sheep:
    def __init__(self, nombre: str, tipo: str = ''):
        self._nombre = nombre
        self._tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
        
    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}'


if __name__ == '__main__':
    original = Sheep('Jolly', 'Dorper')
    print(original)
    #print(original.nombre)
    #print(original.tipo)
    
    print('------')
    cloned = copy.copy(original)
    cloned.nombre = 'Dolly'
    cloned.tipo = 'Suffolk'
    print(cloned)
    #print(cloned.nombre)
    #print(cloned.tipo)
    #print(original.name)
