from Electrodomestico import Electrodomestico

#Clase refrigerador que hereda de la clase Electrodomesticos
class Refrigerador(Electrodomestico)

    def __init__(self, modelo, marca, color, numSerie, voltaje):
        super().__init__(modelo, marca, color, numSerie, voltaje)
        self.cajones = cajones

#Metodos getter y setter para los cajones del refri
    def get_cajones(self):
        return self.cajones

    def set_cajones(self):
        self.cajones = cajones
        
#Metodo que solo manda un mensaje que hizo hielos
    def hacer_hielo (self):
        print("Hielos")
