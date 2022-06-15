from abc import ABC, abstractmethod
from typing import List

# El principio de Abierto/Cerrado básicamente nos dice que una entidad de software (clase, funcion, etc) 
# debe quedar abierta para su extensión pero cerrada para su modificación.
# El códgo anteriror tenía un if anidado por el cual preguntaba por el nombre del animal y en función a eso, 
# imprimía el sinido respectivo del animal. El problema es que rompe con este principio porque hay que modificar
# la función sonido_animal cada vez que se agregue un nuevo animal. 
# Lo que se hizo es crear una interface Animal, para que con la ayuda de polimorfismo, podamos llamar un metodo que se creo para 
# cada animal llamado sound(). 
# Ahora cada vez que se quiera agregar un nuevo sonido no se modificará nada, sólo se agregará una clase Perro, Gato, etc.
# como lo dice el principio.
class Animal(ABC):
    @abstractmethod
    def sound(self) -> None:
        pass

class Leon(Animal):
    def sound(self) -> None:
        print('roar')

class Raton(Animal):
    def sound(self) -> None:
        print('squeak')

def sonido_animal(animales: List[Animal]):
    for animal in animales:
        animal.sound()

animales = [
    Leon(),
    Raton()
]

sonido_animal(animales)