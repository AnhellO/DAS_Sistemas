class ClienteAnimal:

    def __init__(self,animals:list,nombre:str):
        self.animals = animals
        self.nombre = nombre

        def sonido(self):
            count = 0
            for animal in self.animals:
                count += 1

                if animal.get_nombre() == self.nombre:
                    return animal.get_sonido()

                    elif animal.get_nombre() == self.nombre and count == len(self.animals):
                        return "el animal no esta"


def main():
    animales = [
    Perro(),
    gato(),
    puerco();

    ]

    animal = ClienteAnimal(animales,"puerco")

    print(animal.sonido())

    if__name__ == "__main__":
    main()



