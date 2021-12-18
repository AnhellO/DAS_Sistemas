class Auto():
    def __init__(self, constructor, modelo, año):
        self.constructor = constructor
        self.modelo = modelo
        self.año = año   
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.año) + ' ' + self.constructor + ' ' + self.modelo
        return long_name.title()

class Bateria():
    def __init__(self, capacidad=60):
        self.capacidad = capacidad
    def desc(self):
        print("El auto tiene " + str(self.capacidad) + " de Bateria.")   
    def tamañop(self):
        if self.capacidad == 60:
            tamaño = 140
        elif self.capacidad == 85:
            tamaño = 185
            
        message = "Maximo del auto: " + str(tamaño)
        print(message)

    def cambiar_bateria(self):
        if self.capacidad == 60:
            self.capacidad = 85
            print("Bateria actualizada a 85.")
        else:
            print("La batería ya fue actualizada.")
       
class AutoElectrico(Auto):
    def __init__(self, constructor, modelo, año):
        super().__init__(constructor, modelo, año)
        self.Bateria = Bateria()

print("Capacidad de bateria: ")
a1 = AutoElectrico('AstonMartin', 'Modelo 552', 2021)
a1.Bateria.desc()
print("\nBeteria actualizada: ")
a1.Bateria.cambiar_bateria()
a1.Bateria.desc()
print("\nActualizar de nuevo: ")
a1.Bateria.cambiar_bateria()
a1.Bateria.desc()