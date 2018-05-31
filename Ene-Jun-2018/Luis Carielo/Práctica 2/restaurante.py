class Restaurant():
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describe_restaurante(self):
        print("El nombre del restaurante es: " + self.nombre_restaurante.title())
        print("Tipo de comida: " + self.tipo_cocina.title())

    def restaurante_abierto(self):
        print(self.nombre_restaurante.title() + " está abierto.")

#restaurant = Restaurant("El pariente", "mexicana")
#print(restaurant.nombre_restaurante.title() + " | " + restaurant.tipo_cocina.title())
#restaurant.describe_restaurante()
#restaurant.restaurante_abierto()

class IceCreamStand(Restaurant):
    def __init__(self, nombre_restaurante, tipo_cocina="helados"):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = []

    def mostrar_sabores(self):
        print("Los sabores que tiene '" + self.nombre_restaurante + "' son:")
        for x in self.sabores:
            print(x.title())

helados = IceCreamStand("Helados del Ártico")
helados.sabores = ["limón", "coco-nuez", "fresa", "napolitano"]
helados.describe_restaurante()
helados.mostrar_sabores()