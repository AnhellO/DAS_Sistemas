"""
El principio open closed nos dice que
un modulo debe estar abierto a ela extencion de utilidad
pero cerrado a la modificacion del modulo
por lo tanto, la solucion que se nos presenta es la herencia
"""
import abc

class Animal(object):
    def __init__(self, nombre: str, sonido: str):
        self._nombre=nombre
        self._sonido=sonido
    def get_nombre(self) -> str:
        return self._nombre
    def get_sonido(self) -> str:
        return self._sonido

class Animal_Marino(Animal):
    def __init__(self, nombre: str, sonido: str, aletas: int):
        self._nombre=nombre
        self._sonido=sonido
        self._aletas=aletas
    def get_Aletas(self):
        return self._aletas

class Animal_volador(Animal):
    def __init__(self, nombre: str, sonido: str, alas: int):
        self._nombre=nombre
        self._sonido=sonido
        self._alas=alas
    def get_alas(self):
        return self._alas

animales = [
    Animal('león', "roar"),
    Animal('Ratón', "squeak"),
    Animal_Marino("Pez pallaso", "Es una anemona anonima", "3"),
    Animal_volador("chiva", "chsm el america >:V", "2")
]

def sonido_animal(animales: list):
    for animal in animales:
        print(animal._sonido)

sonido_animal(animales)