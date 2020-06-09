class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        pass

    def hacer_sonido(self):
        pass


animales = {
    Animal('león'),
    Animal('ratón'),
    Animal('Vaca')
}


class Leon(Animal):
    def hacer_sonido(self):
        return 'Roar'


class Raton(Animal):
    def hacer_sonido(self):
        return 'Squeak'


class Vaca(Animal):
    def hacer_sonido(self):
        return 'Mooo'


def sonido_animal(animales: list):
    for animal in animales:
        print(animal.hacer_sonido())

    sonido_animal(animales)


""" Al querer utilizar el principio de Open - Closed, las entidades como clases y funciones, deben estar abiertas a la
extensión pero NO a la modificación.
- En el código anterior antes de refactorizarlo, la función de 'sonido_animal' no servía porque cada que se tuviera que 
agregar un animal se iba a tener que estar modificando y eso es lo que debemos evitar. Así que ahora a la clase 'Animal' 
se le agregó el método 'hacer_sonido', con este haremos que cada animal extienda la clase 'Animal' y luego utilice el 
método 'hacer_sonido'.
- Ahora cada animal agrega su propio sonido en 'hacer_sonido' y así cuando agregamos un nuevo animal, la función 
'sonido_animal' no tiene que cambiar. 
"""