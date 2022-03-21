class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        pass
    #En cuanto a esta clase pues funciona para crear un animal, pero el detalle es que esta clase
    #puede ser modificada por fuera sin mucho problema.
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
        #El detalle con esta escalera es que entre mas animales vayan surgiendo mas va a ir creciendo
        #hasta hacerse sumamente enorme, ademas del tamaño del codigo esto aumentaria el tiempo de procesamiento
        #pues así como comienza con un leon y despues un raton... cuando hayan 200 animales va a imprimir ese monton
        #de animales solo para conocer el sonido de 1 solo animal... Eso aparte de tiempo de proceso
        #nos consume memoria que aunque son strings no dejan de consumir mas memoria entre mas strings sean.

sonido_animal(animales)