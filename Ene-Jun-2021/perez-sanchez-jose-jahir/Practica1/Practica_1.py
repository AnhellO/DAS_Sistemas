class Vehiculo():
    random = 0
    def __init__(self,velocidad_maxima, kilometraje, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad
    
    def tarifa(self,capacidad):
        tarifa_i = self.capacidad*100
        return tarifa_i
    
    def __str__(self):
        return f"El Vehiculo tiene una velocidad maxima de: {self.velocidad_maxima}, un kilometraje de: {self.kilometraje} y una capacidad de: {self.capacidad}"

class Autobus(Vehiculo):
    def __init__(self,velocidad_maxima, kilometraje, capacidad):
        super().__init__(velocidad_maxima, kilometraje, capacidad)
    
    def __str__(self):
        return f"Soy un autobus! -> velocidad maxima {self.velocidad_maxima}, kilometraje {self.kilometraje}, capacidad {self.capacidad} "
    


if __name__ == "__main__":
    lista = [
        Vehiculo(100,30000,4),
        Autobus(80,40000,30),
        Vehiculo(180,10000,6),
        Autobus(60,50000,20),
        Vehiculo(180,20000,2),
        Autobus(90,40000,25)
    ]

    
    for x in lista:
        if isinstance(x, Autobus):
            manten = x.tarifa(x.capacidad)*0.1
            tarifa_real = x.tarifa(x.capacidad)+manten 
            print(x,tarifa_real)
