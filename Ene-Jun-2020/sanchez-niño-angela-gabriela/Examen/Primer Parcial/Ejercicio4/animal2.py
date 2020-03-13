
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass
    def sonido(self):
        pass

class Leon(Animal):
    def sonido():
        return 'Leon hace: ROAR'
        
class Raton(Animal):
    def sonido():
        return 'Raton hace: SQUEAK'
animales = [
   Leon,
   Raton
]
def animal_sound(animales: list):
    for animal in animales:
        print(animal.sonido())
animal_sound(animales)

