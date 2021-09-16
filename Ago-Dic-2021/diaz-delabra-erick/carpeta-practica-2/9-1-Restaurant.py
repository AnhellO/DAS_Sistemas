class Restaurant():
    def __init__(self, name, tipo_cocina):
        self.name = name.title()
        self.tipo_cocina = tipo_cocina

    def desc_restaurant(self):
        print("\nEl mejor restaurant de todos! ---> " + self.name + " comida: " + self.tipo_cocina)

    def abierto_restaurant(self):
        print("\n" + self.name + " esta abierto")

restaurant = Restaurant('La cazuela', 'Mexicana')
print(restaurant.name)
print(restaurant.tipo_cocina)

restaurant.desc_restaurant()
restaurant.abierto_restaurant()