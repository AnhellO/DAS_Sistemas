class Animal:
    def __init__(self, nombre: str, sound: str):
        self.nombre = nombre
        self.sound = sound

    def get_nombre(self) -> str:
        return self.nombre

    def get_sound(self) -> str:
        return self.sound
    #se le agego un campo ala clase animal en el momento de crear la coleccion
    #de animales y mostrar todos obtenemos el nombre del animal y su sonido

def main():
    animales = [
        Animal('león','roar'),
        Animal('ratón','squeak'),
        Animal('dog', 'bark'),
        Animal('horse', 'neigh')
    ]
    for animal in animales:
        print(f"animal: {animal.get_nombre()}, sonido: {animal.get_sound()}")

if __name__ == "__main__":
    main()