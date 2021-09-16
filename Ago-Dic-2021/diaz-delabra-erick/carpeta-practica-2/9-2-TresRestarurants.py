class Restaurant():
    def __init__(self, name, tipo_cocina):
        self.name = name.title()
        self.tipo_cocina = tipo_cocina

    def desc_restaurant(self):
        print("\nEl mejor restaurant de todos! ---> " + self.name + " comida: " + self.tipo_cocina)

LaCazuela = Restaurant('La cazuela', 'mexicana')
LaCazuela.desc_restaurant()

dominoes = Restaurant("Dominoes", 'Pizza')
dominoes.desc_restaurant()

sunRoll = Restaurant('SunRoll', 'Sushi')
sunRoll.desc_restaurant()