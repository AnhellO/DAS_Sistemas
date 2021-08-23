class Vehiculo:

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad

        def set_capacidad(self, capacidad):
            self.capacidad = capacidad
        def get_capacidad(self):
            return self.capacidad    
    def tarifa(self, capacidad):
        tarifa = self.capacidad*100
        return tarifa

    random=(50)

    def __str__(self):
       return f"Soy un Vehiculo! -> velocidad maxima {self.velocidad_maxima}, kilometraje {self.kilometraje}, capacidad {self.capacidad} "

class Autobus(Vehiculo):
    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        Vehiculo.__init__(self, velocidad_maxima, kilometraje, capacidad)
        
    def tarifaA(self, capacidad):
        tarifa = super().tarifa(capacidad)
        tarifaA = (tarifa*.1) + tarifa
        return tarifaA 
    def __str__(self):
        return f"Soy un autobus! -> velocidad maxima {self.velocidad_maxima}, kilometraje {self.kilometraje}, capacidad {self.capacidad}"

if __name__=="__main__":
        a1=Autobus(150,25000,30)
        v1=Vehiculo(200,30000,2)
        a2=Autobus(158,55000,40)
        v2=Vehiculo(220,88000,5)
        
        lista_Prueba = [a1,v1,a2,v2]

        for z in lista_Prueba:
            if isinstance(z, Autobus):
                m = z.tarifaA(z.capacidad)
                print(f"{z} -> mi tarifa total es {m} ")
            
            elif isinstance(z, Vehiculo):
                n = z.tarifa(z.capacidad)
                print(f"{z} -> mi tarifa total es {n} ")


