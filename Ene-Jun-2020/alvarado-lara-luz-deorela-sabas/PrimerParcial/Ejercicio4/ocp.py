

class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

    def sonido(self):
        pass
    

animales = [
    Animal('león'),
    Animal('ratón')
]

#CLASE PARA LEON 
class Lion(Animal):
    def sonido(self):
        return 'roar'

#CLASE PARA RATON 
class Mouse(Animal):
    def sonido(self):
        return 'squeak'

def sonido(animales: list):
    for animal in animales:
        print(animal.sonido())

sonido(animales)


"""
La funcion que tenemos para mostrar los sonidos que produce cada animal
no se ajusta al principio O/C ya que si agregamos un nuevo animal tendriamos
que modificar esta misma funcion para cada caso nuevo, lo mismo pasaria 
con los if & elif, cada que se agrega un nuevo elemento se repite una vez mas 
haciendo mas dificil su manipulacion conforme va creciendo la clase.
"""