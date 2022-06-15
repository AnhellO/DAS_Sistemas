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
# lo que va apasar es que la cadena de if y elif se hara mas grande y tedioso y en algunos casos se podrian complicar mas o en pocas palabras ser mas propenso a fallar por ello

sonido_animal(animales)