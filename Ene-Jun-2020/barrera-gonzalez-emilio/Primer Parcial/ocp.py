"""
En respuesta a la  pregunta: Se haría 
"""
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass

animales = [
    Animal('león'),
    Animal('ratón')
]

def sonido_animal(animales: list):
    for animal in animales:
        if animal.nombre == 'león':
            print('roar')

        elif animal.nombre == 'ratón':
            print('squeak')

sonido_animal(animales)