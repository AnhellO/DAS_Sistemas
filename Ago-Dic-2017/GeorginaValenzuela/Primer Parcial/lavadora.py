from electrodomestico import Electrodomestico

#Clase lavadora que hereda de la clase Electrodomesticos
class Lavadora(Electrodomestico)

    def __init__(self, modelo, marca, color, numSerie, voltaje):
        super().__init__(modelo, marca, color, numSerie, voltaje)
        self.ciclos = ciclos

#Metodos getter y setter para los ciclos de la lavadora
    def get_ciclos(self):
        return self.ciclos

    def set_ciclos(self):
        self.ciclos = ciclos
        
#Metodo exprimir solo es un mensaje que nos avisa que esta exprimiendo
    def exprimir (self):
        print("Exprimiento")
