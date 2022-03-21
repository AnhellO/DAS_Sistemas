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


"""Refactoriza el ejemplo proporcionado utilizando el principio Open/Closed (OCP)
de tal forma que podamos agregar más funcionalidad de "animales" sin preocuparnos 
por la modificación de la clase Animal"""