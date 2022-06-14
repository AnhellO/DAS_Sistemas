from animals import Mouse, Lion

if __name__ == '__main__':
    animales = [
        Mouse("Mouse"),
        Lion("Lion")
    ]

    for animal in animales:
        print(animal.make_sound())

# ¿qué pasaría con esa escalera if-elif y en específico con la
# clase Animal si vamos agregando más especies de animales?
#  * Se generaría un codigo Espagueti, que sería difícil depurar.
