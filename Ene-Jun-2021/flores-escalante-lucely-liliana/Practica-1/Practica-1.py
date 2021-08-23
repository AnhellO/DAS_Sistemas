#Parte 1
#Clase Vehículo
class Vehiculo:
    #Atributo Clase
    random= 28
    def __init__(self, velmax, kime, cap):
        #Atributos de instancia
        self.velmax= velmax
        self.kime= kime
        self.cap= cap
   
    def __str__ (self) -> str:
        return f"Velocidad máxima: {self.velmax} km/h, Kilometraje: {self.kime} km, Capacidad: {self.cap}"
    
#Parte 2    
#Clase Autobus hereda a Vehiculo

class Autobus (Vehiculo):
    #Función de monto final
    def tarifa(self):
        tarifa_total= (self.cap*100)
        cargo_mantenimiento= tarifa_total*0.1
        monto_final= tarifa_total + cargo_mantenimiento
        return monto_final
#Parte 3
#Lista de instancias
if __name__ == '__main__':
    Lista_Transportes= [
        Autobus(140, 120000, 15),
        Vehiculo(100, 100000, 3),
        Vehiculo(140, 250000, 5),
        Autobus(100, 400000, 20),
        Autobus(160, 490000, 18),
        Autobus(160, 500000, 16),
        Vehiculo(180, 450000, 2),
        Vehiculo(180, 250000, 1),
        Autobus(80, 500000, 14),
        Vehiculo(160, 450000, 5),
        Vehiculo(180, 750000, 2)
    ]
    #Ciclo para iterar lista
    for trans in Lista_Transportes:
        if isinstance (trans, Autobus):
            print(f"Soy un autobús! -> {trans}")
            trans.tarifa()