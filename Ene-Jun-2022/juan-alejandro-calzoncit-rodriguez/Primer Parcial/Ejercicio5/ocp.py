'''
- ¿Qué pasaría con esa escalera if-elif y en específico con 
  la clase Animal si vamos agregando más especies de animales?
R: Se extendería demasiado la escalera, ya que siempre estará
   verificando el nombre del animal y además agregaría un nuevo
   sonido para cada especie.

'''

class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

# Animales que implementa/heredan de animal
class Pato(Animal):     # Especie pato ya que los informáticos tiene una obsesión con ellos
    def sonido(self):
        print('cuack')

class Leon(Animal):
    def sonido(self): # A cada especie se especifica su sonido
        print('roar')

class Raton(Animal):
    def sonido(self):
        print('squeak')

def sonido_animal(animales: list):
    for animal in animales:
        animal.sonido()

def main():
    animales = [
        Pato('Rubber'),
        Leon('león'),
        Raton('ratón')
    ]
    
    sonido_animal(animales)

    '''
    cuack
    roar
    squeak
    '''

if __name__ == '__main__':
    main()