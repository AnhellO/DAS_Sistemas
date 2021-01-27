class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

animales = [
    Animal('león'),
    Animal('ratón'),
    Animal('gato')

]

def sonido_animal(animales: list):
    for animal in animales:
        if animal.nombre == 'león':
            print('roar')

        elif animal.nombre == 'ratón':
            print('squeak')

        elif animal.nombre == 'gato':
            print('Miau')

        else:
            print('There is not an animal')

sonido_animal(animales)

####### OCP Animal##########

class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

    def hacer_sonido(self):
        pass

class león(Animal):
    def hacer_sonido(self):
        return 'roar'

class ratón(Animal):
    def hacer_sonido(self):
        return 'squeak'

class gato(Animal):
    def hacer_sonido(self):
        return 'miau'

def sonido_animal(animales:list):
    for animal in animales:
        print(animal.hacer_sonido())

sonido_animal(animales)