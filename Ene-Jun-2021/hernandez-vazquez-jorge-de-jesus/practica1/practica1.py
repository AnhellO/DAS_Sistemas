class Vehiculo():
    random = 150
    def __init__(self, vel_max, kmtje, capcty):
        self.vel_max = vel_max
        self.kmtje = kmtje
        self.capcty = capcty
        

    def _str_(self):
        
        return f"""
        La velocidad máxima es: {self.vel_max}Km/h, 
        Kilometraje: {self.kmtje}Km, 
        Capacidad: {self.capcty}
        """
    

class Autobus(Vehiculo):

    def __init__(self, vel_max, kmtje, capcty):
        super().__init__(vel_max, kmtje, capcty)


    
    def tarifa(self):
        cargo_tarifa = self.capcty * 100
        if issubclass(Vehiculo, Autobus):
            mnto_final = cargo_tarifa + (cargo_tarifa * 0.10) 
            return mnto_final 
        return cargo_tarifa

    def __str__(self):
        
        return f"""
        Mi velocidad máxima es de: {self.vel_max}Km/h, 
        Mi Kilometraje es de: {self.kmtje}Km, 
        Capacidad: {self.capcty} asientos,
        La tarifa es de: ${self.tarifa()}  
        """  

if __name__=='__main__':

    vehicles = [  ]
    vehicles.append(Vehiculo(160, 2300, 4)) 
    vehicles.append(Vehiculo(240, 500, 2))
    vehicles.append(Autobus(80, 53000, 15))
    vehicles.append(Autobus(60, 150000, 10))

    vehicles = [print(f'Soy un autobus! {vehicles[i]}') 
                    for i in range(len(vehicles))
                            if isinstance(vehicles[i], Autobus) ]