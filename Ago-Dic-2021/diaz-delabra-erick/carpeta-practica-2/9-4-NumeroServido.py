class Restaurant():
    def __init__(self, nombre, tipo_comida):
        self.nombre = nombre.title()
        self.tipo_comida = tipo_comida
        self.num_servido = 0

    def desc_restaurant(self):
        print("\nEl mejor restaurant de todos! ---> " + self.nombre + " comida: " + self.tipo_comida)

    def abierto(self):
        print("\n" + self.nombre + " esta abierto")

    def numero(self, num_servido):
        self.num_servido = num_servido

    def increment_num_servido(self, x):
        self.num_servido += x

restaurant = Restaurant('La cazuela', 'Mexicana')
restaurant.desc_restaurant()

print("\nNumero sevido: " + str(restaurant.num_servido))
restaurant.num_servido = 1
print("Numero sevido: " + str(restaurant.num_servido))
restaurant.numero(2)
print("Numero sevido: " + str(restaurant.num_servido))
restaurant.increment_num_servido(1)
print("Numero sevido: " + str(restaurant.num_servido))